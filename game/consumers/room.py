from channels.generic.websocket import AsyncWebsocketConsumer
import json

user_ids = {
  "token1": 1,
  "token2": 2,
  "croupier_token1": 3
}

class User():
  def __init__(self, token):
    self.id = user_ids[token]


class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        await self.channel_layer.group_add(
            self.room_id,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_id,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        if self.scope['user'].id:
            await self.parse_message(text_data)
        else:
            try:
                # It means user is not authenticated yet.
                data = json.loads(text_data)
                if 'token' in data.keys():
                    self.scope['user'] = User(data['token'])
            except Exception as e:
                # Data is not valid, so close it.
                print(e)
                pass
        if not self.scope['user'].id:
            self.close()

    async def parse_message(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        if message_type == 'ready':
            if not hasattr(self, 'players'):
                self.players = []
            self.players.append(self.scope['user'])
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_ready',
                    'user_id': self.scope['user'].id
                }
            )
        elif message_type == 'list_players':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'list_players',
                    'players': list(map(lambda u: u.id, self.players))
                }
            )
    
    async def user_ready(self, event):
        await self.send(text_data=json.dumps({
            'status': 'user ' + str(event['user_id']) + ' ready'
        }))

    async def list_players(self, event):
        await self.send(text_data=json.dumps({
            'players': event['players']
        }))