from django.contrib.auth.models import User, Group
from rest_framework import serializers
from location_management.models import * 
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class RegionProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = RegionProject 
    fields = '__all__'
class ZoneProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = ZoneProject 
    fields = '__all__'    
class WeredaProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaProject 
    fields = '__all__'    
class CityProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityProject 
    fields = '__all__'    
class KebeleProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = KebeleProject 
    fields = '__all__' 
class SubCityProjectSerializer(serializers.ModelSerializer):
      class Meta:
       model = SubCityProject 
       fields = '__all__'    
class WeredaKebeleProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model =  WeredaKebeleProject 
    fields = '__all__'     
class CountryProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = CountryProject
    fields = '__all__'   
class CommonSerializer(serializers.ModelSerializer):
     
  class Meta:
    model = object()
    fields = '__all__'   

Meta= object()        
def DynamicSerializerClass(*args):
  global Meta
  Meta = type('Meta', (object, ), dict(model=args[1],fields = args[2],ref_name =args[3]))
  return type(args[0], (CommonSerializer,), dict(Meta=Meta ))