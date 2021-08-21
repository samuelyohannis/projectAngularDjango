from django.contrib.auth.models import User, Group
from rest_framework import serializers
from location_management.models import * 
from .models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
      
""" def DynamicSerializerClass(*args):
      global Meta
  Meta = type('Meta', (object, ), dict(model=args[1],fields = args[2],ref_name =args[3]))
  return type(args[0], (CommonSerializer,), dict(Meta=Meta )) """