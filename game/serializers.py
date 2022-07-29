from rest_framework import serializers

from .models import Room

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'players', 'deck', 'table', 'status', 'bank', 'ante']
