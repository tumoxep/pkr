from rest_framework import serializers

from . import models


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Membership
        fields = ['player', 'room', 'is_ready', 'hand', 'bank', 'action', 'raise_value', 'turn_started', 'acted_last']


class RoomSerializer(serializers.ModelSerializer):
    players = MembershipSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = models.Room
        fields = ['name', 'players', 'table', 'status', 'bank', 'ante', 'turn_timeout']
