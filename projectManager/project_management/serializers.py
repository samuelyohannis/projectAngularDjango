from django.contrib.auth.models import User, Group
from rest_framework import serializers
from location_management.models import * 
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
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

class WeredaKebeleProjectReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaKebeleProjectReport
    fields = '__all__'       

class KebeleProjectReportSerializer(serializers.ModelSerializer):
   class Meta:
    model = KebeleProjectReport
    fields = '__all__'       
class WeredaProjectReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaProjectReport
    fields = '__all__'   
class CityProjectReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityProjectReport
    fields = '__all__'       
class SubCityProjectReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = SubCityProjectReport
    fields = '__all__'   
    
class ZoneProjectReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = ZoneProjectReport
    fields = '__all__'    
    
class RegionProjectReportSerializer(serializers.ModelSerializer):
   class Meta:
    model = RegionProjectReport
    fields = '__all__'                
class CountryProjectReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = CountryProjectReport
    fields = '__all__'
class CountryProjectFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = CountryProjectFile
    fields = '__all__'    
class RegionProjectFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = RegionProjectFile
    fields = '__all__'                            
class CommonSerializer(serializers.ModelSerializer):
     
  class Meta:
    model = object()
    fields = '__all__'   
""" class CountryProjectSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = CountryProject
    fields = '__all__'    """
class CountryProjectSerializer(serializers.ModelSerializer):
  #countryprojectreports = CountryProjectReportSerializer(source='countryprojectreport_set', many=True,)
  """def create(self, validated_data):
        instance = CountryProject.objects.create(**validated_data) """

        #return instance
  def to_representation(self, instance):
        representation = super(CountryProjectSerializer, self).to_representation(instance)
        representation['countryprojectreport'] = CountryProjectReportSerializer(instance.countryprojectreport_set.all(), many=True).data
        representation['countryprojectfile'] = CountryProjectFileSerializer(instance.countryprojectfile_set.all(), many=True).data
        return representation    
  class Meta:
    model = CountryProject
    fields = '__all__'    
class RegionProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = RegionProject 
    fields = '__all__'
  def to_representation(self, instance):
        representation = super(RegionProjectSerializer, self).to_representation(instance)
        representation['regionprojectreport'] = RegionProjectReportSerializer(instance.regionprojectreport_set.all(), many=True).data
        representation['regionprojectfile'] = RegionProjectFileSerializer(instance.regionprojectfile_set.all(), many=True).data
        return representation          
Meta= object()        
def DynamicSerializerClass(*args):
  global Meta
  Meta = type('Meta', (object, ), dict(model=args[1],fields = args[2],ref_name =args[3]))
  return type(args[0], (CommonSerializer,), dict(Meta=Meta ))