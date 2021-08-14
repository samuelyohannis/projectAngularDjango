from django.contrib.auth.models import User, Group
from rest_framework import serializers
from location_management.models import * 
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
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
class ZoneProjectFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = ZoneProjectFile
    fields = '__all__' 
class WeredaProjectFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaProjectFile
    fields = '__all__' 
class CityProjectFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityProjectFile
    fields = '__all__' 
class SubCityProjectFileSerializer(serializers.ModelSerializer):
   class Meta:
    model = SubCityProjectFile
    fields = '__all__' 
    
class KebeleProjectFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = KebeleProjectFile
    fields = '__all__' 
  
class WeredaKebeleProjectFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaKebeleProjectFile
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
      

      
class ZoneProjectSerializer(serializers.ModelSerializer):
  
    
    
  def to_representation(self, instance):
        representation = super(ZoneProjectSerializer, self).to_representation(instance)
        representation['zoneprojectreport'] = ZoneProjectReportSerializer(instance.zoneprojectreport_set.all(), many=True).data
        representation['zoneprojectfile'] = ZoneProjectFileSerializer(instance.zoneprojectfile_set.all(), many=True).data
        return representation     
      
  class Meta:
        model = ZoneProject 
        fields = '__all__'     
class WeredaProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = WeredaProject 
    fields = '__all__'    
    
    
  def to_representation(self, instance):
        representation = super(WeredaProjectSerializer, self).to_representation(instance)
        representation['weredaprojectreport'] = WeredaProjectReportSerializer(instance.weredaprojectreport_set.all(), many=True).data
        representation['weredaprojectfile'] = WeredaProjectFileSerializer(instance.weredaprojectfile_set.all(), many=True).data
        return representation   
      
class CityProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityProject 
    fields = '__all__'  
    
  def to_representation(self, instance):
        representation = super(CityProjectSerializer, self).to_representation(instance)
        representation['cityprojectreport'] = CityProjectReportSerializer(instance.cityprojectreport_set.all(), many=True).data
        representation['cityprojectfile'] = CityProjectFileSerializer(instance.cityprojectfile_set.all(), many=True).data
        return representation   
class KebeleProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = KebeleProject 
    fields = '__all__' 
  def to_representation(self, instance):
        representation = super(KebeleProjectSerializer, self).to_representation(instance)
        representation['kebeleprojectreport'] = KebeleProjectReportSerializer(instance.kebeleprojectreport_set.all(), many=True).data
        representation['kebeleprojectfile'] = KebeleProjectFileSerializer(instance.kebeleprojectfile_set.all(), many=True).data
        return representation 
class SubCityProjectSerializer(serializers.ModelSerializer):
    class Meta:
       model = SubCityProject 
       fields = '__all__'    
       
    def to_representation(self, instance):
        representation = super(SubCityProjectSerializer, self).to_representation(instance)
        representation['subcityprojectreport'] = SubCityProjectReportSerializer(instance.subcityprojectreport_set.all(), many=True).data
        representation['subcityprojectfile'] = SubCityProjectFileSerializer(instance.subcityprojectfile_set.all(), many=True).data
        return representation     
class WeredaKebeleProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model =  WeredaKebeleProject 
    fields = '__all__'     
    def to_representation(self, instance):
        representation = super(WeredaKebeleProjectSerializer, self).to_representation(instance)
        representation['weredakebeleprojectreport'] = WeredaKebeleProjectReportSerializer(instance.weredakebeleprojectreport_set.all(), many=True).data
        representation['weredakebeleprojectfile'] = WeredaKebeleProjectFileSerializer(instance.weredakebeleprojectfile_set.all(), many=True).data
        return representation     
class CityProjectReportFileSerializer(serializers.ModelSerializer):
  class Meta:
    model =  CityProjectReportFile 
    fields = '__all__'     
class CityProjectReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = CityProjectReport
    fields = '__all__'       
       
  def to_representation(self, instance):
        representation = super(CityProjectReportSerializer, self).to_representation(instance)
        representation['cityprojectreportfile'] = CityProjectReportFileSerializer(instance.cityprojectreportfile_set.all(), many=True).data
        return representation         
                   
Meta= object()        
def DynamicSerializerClass(*args):
  global Meta
  Meta = type('Meta', (object, ), dict(model=args[1],fields = args[2],ref_name =args[3]))
  return type(args[0], (CommonSerializer,), dict(Meta=Meta ))