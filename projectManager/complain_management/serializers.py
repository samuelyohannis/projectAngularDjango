
from rest_framework import serializers 
from .models import *

class ProjectComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class RegionProjectComplainSerializer(serializers.ModelSerializer):
  class Meta:
    model = RegionProject 
    fields = '__all__'
class ZoneProjectComplainSerializer(serializers.ModelSerializer):
  class Meta:
    model = ZoneProject 
    fields = '__all__'    
class WeredaProjectComplainSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaProject 
    fields = '__all__'    
class CityProjectComplainSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityProject 
    fields = '__all__'    
class KebeleProjectComplainSerializer(serializers.ModelSerializer):
  class Meta:
    model = KebeleProject 
    fields = '__all__' 
class SubCityProjectComplainSerializer(serializers.ModelSerializer):
      class Meta:
       model = SubCityProject 
       fields = '__all__'    
class WeredaKebeleProjectComplainSerializer(serializers.ModelSerializer):
  class Meta:
    model =  WeredaKebeleProject 
    fields = '__all__'     
class CountryProjectComplainSerializer(serializers.ModelSerializer):
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