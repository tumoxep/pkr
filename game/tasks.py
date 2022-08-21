from enum import Enum
from itertools import chain
from datetime import datetime, timedelta
from django.db.models import Max
from django.utils import timezone
from celery import shared_task

from . import models

class STAGE(Enum):
    PREFLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4


def is_room_ready(room: models.Room):
    total_players = room.players.count()
    if total_players < 2:
        print("room {}: not enough players ({}/2)".format(room.name, total_players))
        return False
    players_ready = room.players.filter(membership__is_ready=True).count()
    if players_ready < total_players:
        print("room {}: not all players ready ({}/{})".format(room.name, players_ready, total_players))
        return False
    return True


def is_royal(player_set):
    return False


def is_straight_flush(player_set):
    return False


def is_four_of_a_kind(player_set):
    return False


def is_full_house(player_set):
    return False


def is_flush(player_set):
    return False


def is_straight(player_set):
    return False


def is_three_of_a_kind(player_set):
    return False


def is_two_pairs(player_set):
    return False


def is_pair(player_set):
    return False


def on_round_finish(room: models.Room):
    scores = {}
    for player in room.players.all():
        player_set = set(list(chain(player.membership_set.get(room=room).hand.all(), room.deck.all()[:5])))
        print("Player set {}".format(player_set))
        if is_royal(player_set):
            scores[player.id] = 10
        elif is_straight_flush(player_set):
            scores[player.id] = 9
        elif is_four_of_a_kind(player_set):
            scores[player.id] = 8
        elif is_full_house(player_set):
            scores[player.id] = 7
        elif is_flush(player_set):
            scores[player.id] = 6
        elif is_straight(player_set):
            scores[player.id] = 5
        elif is_three_of_a_kind(player_set):
            scores[player.id] = 4
        elif is_two_pairs(player_set):
            scores[player.id] = 3
        elif is_pair(player_set):
            scores[player.id] = 2
        else:
            scores[player.id] = 1



@shared_task
def check_player(room_id, position, stage):
    room = models.Room.objects.get(id=room_id)
    player = room.players.get(membership__position=position)
    membership = models.Membership.objects.get(player=player, room=room)
    print("room {}, player {}, position {}, action {}".format(room.name, player.id, position, membership.action))
    if membership.action == '':
        if timezone.now() < room.next_turn:
            print("No action ({}/{})".format(timezone.now(), room.next_turn))
            check_player.apply_async([room.id, position, stage], countdown=1)
            return
        elif room.bet > membership.bet:
            print("No action received. Room's bet ({}) is bigger than player's current bet ({}). Will fold".format(room.bet, membership.bet))
            membership.action = 'f'
            membership.save()
        else:
            print("No action received. Player's bet is enough to check ({}/{}). Check".format(membership.bet, room.bet))
    if membership.action == 'c':
        print("Check ({}/{})".format(membership.bet, room.bet))
        if membership.bet != room.bet:
            print("Wrong action. Will fold")
            membership.action = 'f'
            membership.save()
    if membership.action == 'r':
        if membership.bet >= room.bet:
            print("Bet ({}/{})".format(membership.bet, room.bet))
            room.bet = membership.bet
            room.save()
        elif membership.bet == membership.bank:
            print("Under-bet ({}/{}). All in mode".format(membership.bet, room.bet))
            membership.action = 's'
            membership.save()
        else:
            print("Wrong action. Will fold")
            membership.action = 'f'
            membership.save()
    if membership.action == 'f':
        print("Fold".format(membership.bet, room.bet))
        membership.action = 's'
        membership.bank -= membership.bet
        room.bank += membership.bet
        membership.bet = 0
        room.save()
        membership.save()
    if membership.action != 's':
        print("Not a 'skip' player. Clear action for next turn")
        membership.action = ''
        membership.save()
    player_index = room.players.filter(membership__position__lte=position).count()
    print("player queue ({}/{})".format(player_index, room.players.count()))
    if player_index == room.players.count():
        print("End of player queue")
        max_bet = room.players.aggregate(Max('membership__bet'))['membership__bet__max']
        print("Max bet {}".format(max_bet))
        underbet_players = room.players.filter(membership__bet__lt=max_bet).exclude(membership__action='s')
        if underbet_players.count():
            print("{} underbet players. Repeating trading".format(underbet_players.count()))
            room.next_turn = timezone.now() + timedelta(seconds=room.timeout)
            room.save()
            check_player.apply_async([room.id, 1, stage])
            return
        elif stage == STAGE.RIVER.value:
            on_round_finish()
        service_game.apply_async([room.id, stage + 1])
        return
    room.next_turn = timezone.now() + timedelta(seconds=room.timeout)
    room.save()
    print("Switching to the next player".format(timezone.now(), room.next_turn))
    check_player.apply_async([room.id, position + 1, stage])


@shared_task
def service_game(room_id, stage):
    room = models.Room.objects.get(id=room_id)
    print("room {}: service_game. stage={}".format(room.name, stage))
    players = room.players.filter(membership__bank__gte=room.blind)
    if players.count() < 2:
        room.status = 'w'
        room.save()
        return
    if stage == STAGE.PREFLOP.value:
        models.CardInDeck.objects.filter(room=room).delete()
        for card in models.Card.objects.order_by('?'):
            models.CardInDeck.objects.create(card=card, room=room)
        position = 1
        for player in players:
            membership = models.Membership.objects.get(player=player, room=room)
            membership.position = position
            membership.hand.set(room.deck.order_by('cardindeck__position')[:2])
            models.CardInDeck.objects.filter(pk__in=models.CardInDeck.objects.filter(room=room).order_by('position')[:2]).delete()
            if position == 1:
                membership.bank -= room.blind
                room.bank += room.blind
            if position == 2:
                membership.bank -= (room.blind / 2)
                room.bank += (room.blind / 2)
            membership.action = ''
            membership.bet = 0
            membership.save()
            room.save()
            position += 1
            print("room {}: player {}, hand {}".format(room.name, player.id, membership.hand))
    if stage == STAGE.FLOP.value:
        room.table.add(*room.deck.order_by('cardindeck__position')[:3])
        models.CardInDeck.objects.filter(pk__in=models.CardInDeck.objects.filter(room=room).order_by('position')[:3]).delete()
    if stage == STAGE.TURN.value or stage == STAGE.RIVER.value:
        room.table.add(*room.deck.order_by('cardindeck__position')[:1])
        models.CardInDeck.objects.filter(pk__in=models.CardInDeck.objects.filter(room=room).order_by('position')[:1]).delete()
    room.next_turn = timezone.now() + timedelta(seconds=room.timeout)
    room.save()
    check_player.apply_async([room.id, 1, stage])


@shared_task
def service_room(room_id):
    room = models.Room.objects.get(id=room_id)
    if room.status == 'w':
        if not is_room_ready(room):
            return
        room.status = 'r'
        room.save()
        return
    elif room.status == 'r':
        room.status = 'c'
        room.save()
        service_game.apply_async([room.id, STAGE.PREFLOP.value])
        return


@shared_task
def check_rooms():
    rooms = models.Room.objects.all()
    for room in rooms:
        service_room.apply_async([room.id])
