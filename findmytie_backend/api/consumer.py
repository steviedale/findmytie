# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Process the received data and semessages back to the client
        print(f"Received data: {data}")
        await self.send(text_data=json.dumps(['kenny', 'madi', 'devon', 'ryan']))
        print('done with recieve().')


# # consumer.py
# from channels.consumer import SyncConsumer

# class EchoConsumer(SyncConsumer):

#     def websocket_connect(self, event):
#         self.send({
#             "type": "websocket.accept",
#         })

#     def websocket_receive(self, event):
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })