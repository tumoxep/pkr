from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    class Cards(models.TextChoices):
        cC2 = 'C2', _('2 of clubs')
        cC3 = 'C3', _('3 of clubs')
        cC4 = 'C4', _('4 of clubs')
        cC5 = 'C5', _('5 of clubs')
        cC6 = 'C6', _('6 of clubs')
        cC7 = 'C7', _('7 of clubs')
        cC8 = 'C8', _('8 of clubs')
        cC9 = 'C9', _('9 of clubs')
        cCX = 'CX', _('10 of clubs')
        cCJ = 'CJ', _('J of clubs')
        cCQ = 'CQ', _('Q of clubs')
        cCK = 'CK', _('K of clubs')
        cCA = 'CA', _('A of clubs')
        cD2 = 'D2', _('2 of diamonds')
        cD3 = 'D3', _('3 of diamonds')
        cD4 = 'D4', _('4 of diamonds')
        cD5 = 'D5', _('5 of diamonds')
        cD6 = 'D6', _('6 of diamonds')
        cD7 = 'D7', _('7 of diamonds')
        cD8 = 'D8', _('8 of diamonds')
        cD9 = 'D9', _('9 of diamonds')
        cDX = 'DX', _('10 of diamonds')
        cDJ = 'DJ', _('J of diamonds')
        cDQ = 'DQ', _('Q of diamonds')
        cDK = 'DK', _('K of diamonds')
        cDA = 'DA', _('A of diamonds')
        cH2 = 'H2', _('2 of hearts')
        cH3 = 'H3', _('3 of hearts')
        cH4 = 'H4', _('4 of hearts')
        cH5 = 'H5', _('5 of hearts')
        cH6 = 'H6', _('6 of hearts')
        cH7 = 'H7', _('7 of hearts')
        cH8 = 'H8', _('8 of hearts')
        cH9 = 'H9', _('9 of hearts')
        cHX = 'HX', _('10 of hearts')
        cHJ = 'HJ', _('J of hearts')
        cHQ = 'HQ', _('Q of hearts')
        cHK = 'HK', _('K of hearts')
        cHA = 'HA', _('A of hearts')
        cS2 = 'S2', _('2 of spades')
        cS3 = 'S3', _('3 of spades')
        cS4 = 'S4', _('4 of spades')
        cS5 = 'S5', _('5 of spades')
        cS6 = 'S6', _('6 of spades')
        cS7 = 'S7', _('7 of spades')
        cS8 = 'S8', _('8 of spades')
        cS9 = 'S9', _('9 of spades')
        cSX = 'SX', _('10 of spades')
        cSH = 'SH', _('J of shearts')
        cSQ = 'SQ', _('Q of spades')
        cSK = 'SK', _('K of spades')
        cSA = 'SA', _('A of spades')

    value = models.CharField(max_length=2, choices=Cards.choices)


class Room(models.Model):
    name = models.CharField(max_length=200, default='')
    players = models.ManyToManyField(User, through='RoomMembership', related_name='+')
    table = models.ManyToManyField(Card, through='RoomTableCard', related_name='+')
    ante = models.IntegerField(default=0)
    bank = models.IntegerField(default=0)
    turn_timeout = models.IntegerField(default=30)
    
    class RoomStatuses(models.TextChoices):
        WAIT = 'wt', _('waiting for players')
        PREFLOP = 'pf', _('preflop')
        FLOP = 'fp', _('flop')
        TURN = 'tn', _('turn')
        RIVER = 'rv', _('river')
        IDLE = 'no', _('idle')

    status = models.CharField(
        max_length=2,
        choices=RoomStatuses.choices,
        default=RoomStatuses.IDLE,
    )


class RoomMembership(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_ready = models.BooleanField(default=False)
    bank = models.IntegerField(default=0)
    raise_value = models.IntegerField(default=0)
    
    class RoomMemberActions(models.TextChoices):
        BET = 'bet', _('bet')
        CALL = 'call', _('call')
        RAISE = 'raise', _('raise')
        CHECK = 'check', _('check')
        FOLD = 'fold', _('fold')

    action = models.CharField(
        max_length=5,
        choices=RoomMemberActions.choices,
        default=RoomMemberActions.FOLD,
    )
    turn_started = models.DateTimeField(null=True)
    acted_last = models.DateTimeField(null=True)

    class RoomMemberRoles(models.TextChoices):
        S_BLIND = 's', _('small blind')
        B_BLIND = 'b', _('big blind')
        DEFAULT = 'd', _('default')

    role = models.CharField(
        max_length=1,
        choices=RoomMemberRoles.choices,
        default=RoomMemberRoles.DEFAULT,
    )


class RoomTableCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
