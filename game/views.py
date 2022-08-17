from rest_framework import viewsets

from . import models
from . import serializers

class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = models.Membership.objects.all()
    serializer_class = serializers.MembershipSerializer
