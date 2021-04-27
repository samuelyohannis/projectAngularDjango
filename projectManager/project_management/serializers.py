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
class CountryProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = CountryProject
    fields = '__all__'   
