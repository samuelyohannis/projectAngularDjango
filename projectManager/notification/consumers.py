
from user_management.models import Profile
from project_management.serializers import CountryProjectReportSerializer
from project_management.models import CountryProjectReport
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer
# from channels.generic.websocket import WebsocketDemultiplexe
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver,Signal
from project_management.models import CountryProject
from project_management.serializers import CountryProjectSerializer
from asgiref.sync import async_to_sync, sync_to_async
from notification_management.models import Notification
from user_management.serializers import UserSerializer,ProfileSerializer
from notification_management.serializers import *
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
import uuid
import json
gb =  globals()
ctx={}
class NotificationConsumer(AsyncWebsocketConsumer):
  
   async def connect(self,):
       gb['cxt']=self
       self.room_name = self.scope['url_route']['kwargs']['group_name']   
       #    self.room_group_name = 'notification_%s' % self.room_name
       self.room_group_name = 'notification_'+ self.room_name
           
       
       await self.channel_layer.group_add(self.room_group_name,self.channel_name)
       await self.accept() 
      
       await self.channel_layer.group_send(self.room_group_name,
                                           {"type":"notications","notications":"You are connected to notification stream"}) 
       self.uuid3=[]
       def my(sender,instance=None,created=None,dispatch_uid=None,**kwargs,) :
            
            print(self.room_group_name)
            instance =NotificationSerializer(instance).data
            if created == True:
             async_to_sync(self.send)(text_data=json.dumps({"Notification":instance})) 
             self.uuid3 = dispatch_uid
       if self.room_group_name == f'notification_country_{self.scope["user"].id}':
            await sync_to_async(post_save.connect)(my,sender=Notification,dispatch_uid=uuid.uuid4(),weak=False)      
       if self.room_group_name == "notification_country_project_manager":
            await sync_to_async(post_save.connect)(my,sender=Notification,dispatch_uid=uuid.uuid4(),weak=False)
  
   @database_sync_to_async
   def get_notifications(self):
        return Notification.objects.all()
   
   @database_sync_to_async
   def get_serialized_notifications(self):
    return NotificationSerializer(Notification.objects.all(),many=True).data

   @database_sync_to_async
   def get_serialized_user(self,id):
    return UserSerializer(User.objects.get(pk=id)).data

   @database_sync_to_async
   def get_serialized_profile(self,id):
    return ProfileSerializer(Profile.objects.get(pk=id)).data

   @database_sync_to_async
   def get_serialized_current_user(self):
    return UserSerializer(User.objects.get(pk=self.scope["user"].id)).data

   @database_sync_to_async
   def get_serialized_current_profile(self):
    return ProfileSerializer(Profile.objects.get(user=self.scope["user"].id)).data

   async def notications(self,event):
          notifications = await self.get_serialized_notifications()
          await self.send(text_data=json.dumps({"notifications":notifications,"message":"You are connected to notification stream"}))
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
        
class ProjectNotification(AsyncWebsocketConsumer):
      
   async def connect(self,):
       gb['cxt']=self
       self.room_name = self.scope['url_route']['kwargs']['group_name']   
       #    self.room_group_name = 'notification_%s' % self.room_name
       self.room_group_name = 'project_notification_'+ self.room_name
           
       
       await self.channel_layer.group_add(self.room_group_name,self.channel_name)
       await self.accept() 
       await self.channel_layer.group_send(self.room_group_name,
                                           {"type":"test1","tester":"You are connected to project notification stream"}) 
       self.uuid1=None
       
       def projectSignalCallback(sender,instance=None,dispatch_uid=None,**kwargs) :
           
            print('check my Signal')
            print(self.room_group_name)
            instance =CountryProjectSerializer(instance).data 
            if self.uuid1 != dispatch_uid:
             async_to_sync(self.send)(text_data=json.dumps({"Notification":instance})) 
             self.uuid1 = dispatch_uid
       if self.room_group_name == 'project_notification_project':
        await sync_to_async(post_save.connect)(projectSignalCallback,sender=CountryProject,dispatch_uid=uuid.uuid4(),weak=False)
       self.uuid2=None
       def projectReportSignalCallback(sender,instance=None,dispatch_uid=None,**kwargs) :
            
            print('check my Signal')
            print(self.room_group_name)
            instance =CountryProjectReportSerializer(instance).data 
            if self.uuid2 != dispatch_uid:
             async_to_sync(self.send)(text_data=json.dumps({"Notification":instance})) 
             self.uuid2 = dispatch_uid
       if self.room_group_name == 'project_notification_project_report':
        await sync_to_async(post_save.connect)(projectReportSignalCallback,sender=CountryProjectReport,dispatch_uid=uuid.uuid4(),weak=False)
    
   async def test1(self,event):
          tester = event['tester'] 
          await self.send(text_data=json.dumps({"tester":tester,"projects":[]})) 
   
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
        
        
class NotificationConsumer1(WebsocketConsumer):
      
   def connect(self,):
   
       self.room_name = self.scope['url_route']['kwargs']['group_name']   
       self.group_name = 'notification_'+ self.scope['url_route']['kwargs']['group_name']
    #    self.room_group_name = 'notification_'+ self.room_name
           
       
       async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
    
       self.accept() 
       
      
        # @receiver(post_save,sender=CountryProject,weak=False)
 
       def my(sender,**kwargs) :
            print('check my Signal')
            print(self.group_name)
        
            self.send(text_data=json.dumps({"tester":'dedeb'}))  
       '''  async_to_sync(self.channel_layer.group_send)('notification_sav',
                                           {"type":"test1","tester":"sam"} ) '''
        
       if self.group_name == 'notification_sav':
        post_save.connect(my,sender=CountryProject,dispatch_uid=uuid.uuid4())  
 
   
   def test1(self,event):
          tester = event['tester'] 
          self.send(text_data=json.dumps({"tester":tester}))  
   def test(self,event):
          tester = event['tester'] 
          self.send(text_data=json.dumps({"tester":tester}))
        
          
    
   def disconnect(self, close_code):
       async_to_sync(self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        ))

   def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))