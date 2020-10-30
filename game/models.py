from django.db import models

class Room(models.Model):
    url = models.CharField('room url', max_length=200, default='')
    name = models.CharField('room name', max_length=200, default='')
    state = models.JSONField('current state', null=True)
    bank = models.PositiveIntegerField('current bank', default=0)
    deck = models.JSONField('current deck', null=True)
    table = models.JSONField('current table', null=True)
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField('player name', max_length=200, default='')
    decision = models.JSONField('current decision', null=True)
    hand = models.JSONField('current hand', null=True)
    wallet = models.PositiveIntegerField('current wallet', default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    ready = models.BooleanField('is player ready', default=False)
    def __str__(self):
        return self.name
