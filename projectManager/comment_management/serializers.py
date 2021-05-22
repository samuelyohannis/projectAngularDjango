from django.contrib.auth.models import User, Group
from rest_framework import serializers 
from .models import *

class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = '__all__'
class RegionProjectCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = RegionProjectComment 
    fields = '__all__'
class ZoneProjectCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = ZoneProjectComment 
    fields = '__all__'    
class WeredaProjectCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaProjectComment 
    fields = '__all__'    
class CityProjectCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityProjectComment 
    fields = '__all__'    
class KebeleProjectCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = KebeleProjectComment 
    fields = '__all__' 
class SubCityProjectCommentSerializer(serializers.ModelSerializer):
      class Meta:
       model = SubCityProjectComment 
       fields = '__all__'    
class WeredaKebeleProjectCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model =  WeredaKebeleProjectComment 
    fields = '__all__'     
class CountryProjectCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = CountryProjectComment
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