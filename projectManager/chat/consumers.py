from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer
# from channels.generic.websocket import WebsocketDemultiplexe

import json
class ChatRoomConsumer(AsyncWebsocketConsumer):
   async def connect(self,):
      
       self.room_name = self.scope['url_route']['kwargs']['room_name']   
       self.room_group_name = 'chat_%s' % self.room_name
      
      
       
       await self.channel_layer.group_add(self.room_group_name,self.channel_name)
       await self.accept() 
       await self.channel_layer.group_send(self.room_group_name,
                                           {"type":"test","tester":"sam"})
      
   async def test(self,event):
          tester = event['tester'] 
          await self.send(text_data=json.dumps({"tester":tester}))   

   async def disconnect(self, close_code):
       await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

   async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))