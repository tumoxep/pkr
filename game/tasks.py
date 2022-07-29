from celery import shared_task

from . import models


@shared_task
def check_rooms():
    rooms = models.Room.objects.all()
    for room in rooms:
        print("room: {}, status: {}".format(room.name, room.status))
