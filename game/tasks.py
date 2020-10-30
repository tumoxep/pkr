from background_task import background
from .models import Player
from .models import Room

@background(schedule=30)
def check_players(room_id):
    players = Player.objects.filter(room=room_id)
    if len(players) > 1:
        check_ready()
    else:
        check_players()

@background(schedule=30)
def check_ready(room_id, ):
    players = Player.objects.filter(room=room_id)
    for p in players.filter(ready=False):
        # kick_player(room_id, p)
    if len(players.filter(ready=True)) > 1:
        start_game()
    else:
        check_players()

def start_game(room_id):
    room = Room.objects.get(id=room_id)
    # room.deck = get_deck()
    # room.save()
    players = Player.objects.all(room=room_id)
    for p in players.filter(ready=True):
        # p.hand = get_hand()
        # p.save()
