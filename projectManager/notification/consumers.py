
from user_management.models import Profile
from project_management.serializers import CountryProjectReportSerializer
from project_management.models import CountryProjectReport
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer
# from channels.generic.websocket import WebsocketDemultiplexe
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver,Signal
from project_management.models import CountryProject,CountryProjectNotification
from project_management.serializers import CountryProjectSerializer,CountryProjectNotificationSerializer
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
       self.user = self.scope['user']
       #    self.room_group_name = 'notification_%s' % self.room_name
       self.room_group_name = 'notification_'+ self.room_name
           
       
       await self.channel_layer.group_add(self.room_group_name,self.channel_name)
       await self.accept() 
      
       await self.channel_layer.group_send(self.room_group_name,
                                           {"type":"asyncGetProfile"})
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
    print(self.user.id)
    return ProfileSerializer(Profile.objects.filter(user=self.user.id),many=True).data

   async def notications(self,event):
          notifications = await self.get_serialized_notifications()
          await self.send(text_data=json.dumps({"notifications":notifications,"message":"You are connected to notification stream"}))
   async def asyncGetProfile(self,event):
          tester = await self.get_serialized_current_profile()
          await self.send(text_data=json.dumps({"profile":tester}))   
        
          
    
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
       self.room_name = self.scope['url_route']['kwargs']['group_name'] 
       self.profile_id = self.scope['url_route']['kwargs']['profile_id']   
       self.group_name = 'notification_'+ self.scope['url_route']['kwargs']['group_name']
      
           
       
       await self.channel_layer.group_add(self.group_name,self.channel_name)
       await self.accept() 
       await self.channel_layer.group_send(self.group_name,{"type":"sendSelfNotification"}) 
       
                                           
       self.uuid3=[]
       def my(sender,instance=None,created=None,dispatch_uid=None,**kwargs,) :
            
            print(self.room_group_name)
            instance =NotificationSerializer(instance).data
            if created == True:
             async_to_sync(self.send)(text_data=json.dumps({"Notification":instance})) 
             self.uuid3 = dispatch_uid
           
       def user_logged(sender,user=None,dispatch_uid=None,**kwargs,) :
            
             print('i am user')
             instance =UserSerializer(user).data 
             print(instance)
             async_to_sync(self.send)(text_data=json.dumps({"User":instance})) 
             self.uuid3 = dispatch_uid
       await sync_to_async(user_logged_in.connect)(user_logged,weak=False,dispatch_uid=uuid.uuid4(),sender=User)
          
       if self.group_name == f'notification_country_{self.scope["user"].id}':
            await sync_to_async(post_save.connect)(my,sender=Notification,dispatch_uid=uuid.uuid4(),weak=False)      
       if self.group_name == "notification_country_project_manager":
            await sync_to_async(post_save.connect)(my,sender=Notification,dispatch_uid=uuid.uuid4(),weak=False)
       #   await sync_to_async(user_logged_out.connect)(user_logged,dispatch_uid=uuid.uuid4(),weak=False)   

   @database_sync_to_async
   def get_notifications(self):
        return CountryProjectNotification.objects.all()
   
   @database_sync_to_async
   def get_self_projects(self):
        return CountryProjectSerializer(CountryProject.objects.filter(profile=self.profile_id),many=True).data 
   @database_sync_to_async
   def get_self_project_reports(self):
        return CountryProjectReportSerializer(CountryProjectReport.objects.filter(profile=self.profile_id),many=True).data 
   @database_sync_to_async
   def get_self_notifications(self):
        return CountryProjectNotificationSerializer(CountryProjectNotification.objects.filter(send_to=self.profile_id),many=True).data 
   async def sendSelfNotification(self,event):
          
          notifications = await self.get_self_notifications()
          projects = await self.get_self_projects()
          print('i am recent')
          project_reports = await self.get_self_project_reports()     
          await self.send(text_data=json.dumps({"user_notifications":notifications,"user_reports":project_reports,"user_projects":projects})) 
   
   
        
          
    
   async def disconnect(self, close_code):
       await self.channel_layer.group_discard(
            self.group_name,
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
       self.profile_id = self.scope['url_route']['kwargs']['profile_id']   
       self.group_name = 'notification_'+ self.scope['url_route']['kwargs']['group_name']
    #    self.room_group_name = 'notification_'+ self.room_name
 
       
       async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
    
       self.accept() 
       async_to_sync(self.channel_layer.group_send)(self.group_name,
                                           {"type":"profile"})
      
       # @receiver(post_save,sender=CountryProject,weak=False)
 
       def my(sender,**kwargs) :
            """ print('check my Signal')
            print(self.group_name)
         """
            self.send(text_data=json.dumps({"tester": self.scope['user']}))  
       '''  async_to_sync(self.channel_layer.group_send)('notification_sav',
                                           {"type":"test1","tester":"sam"} ) '''
        
       if self.group_name == 'notification_sav':
        post_save.connect(my,sender=CountryProject,dispatch_uid=uuid.uuid4())  
 
   def get_serialized_current_profile(self):
        print(self.profile_id) 
        return ProfileSerializer(Profile.objects.get(pk= self.profile_id )).data
   def profile(self,event):
     
          self.send(text_data=json.dumps({"profile": self.get_serialized_current_profile()}))  
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

        
class DynamicConsumer(WebsocketConsumer):
     
   def connect(self,):
   
       self.room_name = self.scope['url_route']['kwargs']['group_name'] 
       self.profile_id = self.scope['url_route']['kwargs']['profile_id']   
       self.group_name = 'notification_'+ self.scope['url_route']['kwargs']['group_name']
    #    self.room_group_name = 'notification_'+ self.room_name
       self.user = self.scope["user"]    
       
       async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
    
       self.accept() 
       async_to_sync(self.channel_layer.group_send)(self.group_name,
                                           {"type":"profile"})
      
       # @receiver(post_save,sender=CountryProject,weak=False)
 
       def my(sender,**kwargs) :
            """ print('check my Signal')
            print(self.group_name)
         """
            self.send(text_data=json.dumps({"tester": self.scope['user']}))  
       '''  async_to_sync(self.channel_layer.group_send)('notification_sav',
                                           {"type":"test1","tester":"sam"} ) '''
        
       if self.group_name == 'notification_sav':
        post_save.connect(my,sender=CountryProject,dispatch_uid=uuid.uuid4())  
 
   def get_serialized_current_profile(self):
        print(self.profile_id) 
        return ProfileSerializer(Profile.objects.get(pk= self.profile_id )).data
   def profile(self,event):
     
          self.send(text_data=json.dumps({"profile": self.get_serialized_current_profile()}))  
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
              
        
   def dynamicConsumer(*args):
       
     return  type('',   (DynamicConsumer,), dict(k='') )    