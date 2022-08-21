from turtle import position
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

score_to_value = {
    10: 'Jack',
    11: 'Queen',
    12: 'King',
    13: 'ace',
}

class Card(models.Model):
    class Suits(models.TextChoices):
        CLUBS = 'c', _('♣')
        DIAMONDS = 'd', _('♦')
        HEARTS = 'h', _('♥')
        SPADES = 's', _('♠')

    score = models.IntegerField()
    suit = models.CharField(
        max_length=1,
        choices=Suits.choices,
    )

    def __str__(self):
        value = self.score + 1
        if self.score > 9:
            value = score_to_value[self.score]
        return "{}{}".format(value, self.get_suit_display())


class Room(models.Model):
    name = models.CharField(max_length=200, default='')
    players = models.ManyToManyField(User, through='Membership', related_name='+')
    deck = models.ManyToManyField(Card, through='CardInDeck', related_name='+')
    table = models.ManyToManyField(Card, related_name='+', null=True, blank=True)
    blind = models.IntegerField(default=10)
    ante = models.IntegerField(default=0)
    bank = models.IntegerField(default=0)
    next_turn = models.DateTimeField(null=True, blank=True)
    bet = models.IntegerField(default=0)
    timeout = models.IntegerField(default=30)
    
    class RoomStatuses(models.TextChoices):
        WAITING = 'w', _('waiting for players')
        READY = 'r', _('ready')
        UNDER_CONTROL = 'c', _('under control')
        ENDED = 'e', _('ended')

    status = models.CharField(
        max_length=1,
        choices=RoomStatuses.choices,
        default=RoomStatuses.WAITING,
    )


class Membership(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_ready = models.BooleanField(default=False)
    bank = models.IntegerField(default=100)
    bet = models.IntegerField(default=0)
    hand = models.ManyToManyField(Card, related_name='+', null=True, blank=True)
    position = models.IntegerField(default=0)
    
    class MemberActions(models.TextChoices):
        RAISE = 'r', _('raise')
        CHECK = 'c', _('check')
        FOLD = 'f', _('fold')
        SKIP = 's', _('skp')
        NO_ACTION = '', _('no action')

    action = models.CharField(
        max_length=1,
        choices=MemberActions.choices,
        default=MemberActions.FOLD,
    )


class CardInDeck(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
