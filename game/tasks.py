from turtle import position
from celery import shared_task

from . import models

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


@shared_task
def service_game(room_id, stage):
    room = models.Room.objects.get(id=room_id)
    print("room {}: service_game. stage={}".format(room.name, stage))
    if stage == 'preflop':
        position = 1
        for card in models.Card.objects.order_by('?'):
            models.CardInDeck.objects.create(card=card, room=room, position=position)
            position += 1
        position = 1
        card_pos = 1
        for player in room.players.all():
            card1 = models.CardInDeck.objects.get(room=room, position=card_pos)
            card_pos += 1
            card2 = models.CardInDeck.objects.get(room=room, position=card_pos)
            membership = models.Membership.objects.get(player=player, room=room)
            membership.hand.set([card1.card, card2.card])
            room.deck.remove(card1.card)
            room.deck.remove(card2.card)
            if position == 1:
                membership.bank -= room.blind
                room.bank += room.blind
            if position == 2:
                membership.bank -= (room.blind / 2)
                room.bank += (room.blind / 2)
            membership.save()
            room.save()
            card_pos += 1
            position += 1
            print("room {}: player {}, hand {}".format(room.name, player.id, membership.hand))
    room.status = 'c' # e
    room.save()



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
        service_game.apply_async([room.id, 'preflop'])
        return


@shared_task
def check_rooms():
    rooms = models.Room.objects.all()
    for room in rooms:
        service_room.apply_async([room.id])
