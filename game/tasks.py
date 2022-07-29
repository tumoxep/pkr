from datetime import datetime
from celery import shared_task

from . import models

def are_players_ready(room: models.Room):
    return room.players.count >= 2 and room.players.filter(is_ready=False)


@shared_task
def service_preflop(room: models.Room):
    current_player = room.players.get(turn_started__isnull=False)
    delta = datetime.now() - current_player.turn_started
    if delta.total_seconds() > room.turn_timeout:
        current_player.turn_started = None
        #
        return
    elif current_player.acted_last > current_player.turn_started:
        current_player.turn_started = None
        #
        return


@shared_task
def service_room(room: models.Room):
    if room.status == 'no':
        return
    elif room.status == 'wt':
        if are_players_ready(room):
            room.status = 'pf'
            room.save()
            return
    elif room.status == 'pf':
        service_preflop(room)
        return


@shared_task
def check_rooms():
    rooms = models.Room.objects.all()
    for room in rooms:
        service_room.apply_async(room)
