import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import datetime


# async class implementation
class ChatConsumer(AsyncWebsocketConsumer):
    room_group_name = "ftp"
    async def connect(self):
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

    # Receive message from WebSocket(from client)
    async def receive(self, **kwargs):
        def handle_uploaded_file(f):
            with open('some_file.jpg', 'wb+') as destination:
                destination.write(f)
        print(f"kwargs: {kwargs.keys()}")

        print(f"scope of channel")
        if 'bytes_data' in kwargs.keys():
            print(f"image data type: {type(kwargs['bytes_data'])} ")
            handle_uploaded_file(kwargs['bytes_data'])
            time =  datetime.datetime.now().strftime("%H:%M:%S")
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'image':  kwargs['bytes_data']
                }
            )
        else:
            text_data_json = json.loads(kwargs['text_data'])
            print(text_data_json)
            message = f"{self.scope['user']}: " + text_data_json['message']
        
            # Send message to room group
            time =  datetime.datetime.now().strftime("%H:%M:%S")
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message + f"\t\t\t {time}",
                }
            )

    # Receive message from room group(internally)
    async def chat_message(self, event):
        print(f"event_keys: {event.keys()}")
        if 'image' in event.keys():
            image = event['image']
            print(f"image:{type(image)}")
            await self.send(bytes_data=image)
        else:
            message = event['message']
            print(f"message received: {message}")
            count = getattr(self.channel_layer, self.room_group_name, 0)
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'image': "some-image.jpg",
                'count': count, 
            }))

    