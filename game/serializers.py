from rest_framework import serializers

from . import models

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Room
        fields = ['name', 'players', 'deck', 'table', 'status', 'bank', 'ante']

class RoomMembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RoomMembership
        fields = ['player', 'room', 'is_ready', 'hand', 'bank', 'role', 'action', 'raise_value']
