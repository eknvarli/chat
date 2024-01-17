import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from rooms.models import Room, Message
from core.models import CustomUser

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'room':room
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']


        # emojis
        if ':D' in message:
            message = message.replace(':D','😃')
        elif ';)' in message:
            message = message.replace(';)','😏')
        elif ':)' in message:
            message = message.replace(':)','🙂')
        elif '<3' in message:
            message = message.replace('<3','❤️')
        elif '::cool' in message:
            message = message.replace('::cool','😎')
        elif '::star' in message:
            message = message.replace('::star','⭐')
        
        elif 'http://' in message:
            message = 'I share http link, but George stopped me.'

        if message.startswith('https'):
            message = f'<a target="_blank" href={message}>{message}</a>'

        await self.save_message(username, room, message)

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'room':room
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = CustomUser.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)