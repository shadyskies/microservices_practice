import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import datetime


# async class implementation
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope['user'])
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        count = getattr(self.channel_layer, self.room_group_name, 0)
        if not count:
            setattr(self.channel_layer, self.room_group_name, 1)
        else:
            setattr(self.channel_layer, self.room_group_name, count + 1)
        print(count)
        time =  datetime.datetime.now().strftime("%H:%M:%S")

        #send room connect message
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f"{self.scope['user']} has joined the channel \t\t\t{time}",
                'count': count
            }
        )

    async def disconnect(self, close_code):
        time =  datetime.datetime.now().strftime("%H:%M:%S")
        count = getattr(self.channel_layer, self.room_group_name, 0)
        if not count:
            setattr(self.channel_layer, self.room_group_name, 1)
        else:
            setattr(self.channel_layer, self.room_group_name, count - 1)
       
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'chat_message',
                'message': f"{self.scope['user']} has left the channel \t\t\t{time}",
                'count': count
            }
        )
        print(f"closed websocket with code: {close_code}")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = f"{self.scope['user']}: " + text_data_json['message']
       
        # Send message to room group
        time =  datetime.datetime.now().strftime("%H:%M:%S")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message + f"\t\t\t {time}"
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        print(event)
        count = getattr(self.channel_layer, self.room_group_name, 0)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'count': count
        }))
