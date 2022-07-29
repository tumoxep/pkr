from rest_framework import viewsets

from . import models
from . import serializers

class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

class RoomMembershipViewSet(viewsets.ModelViewSet):
    queryset = models.RoomMembership.objects.all()
    serializer_class = serializers.RoomMembershipSerializer
