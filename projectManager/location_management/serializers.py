from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'
class WeredaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wereda
        fields = '__all__'
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'                
class SubCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCity
        fields = '__all__'
class KebeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kebele
        fields = '__all__'  
class WeredaKebeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeredaKebele
        fields = '__all__'               