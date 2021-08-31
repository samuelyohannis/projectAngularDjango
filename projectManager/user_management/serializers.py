from subscription.serializers import SubscriptionSerializer
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields =  '__all__'
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields =  '__all__'
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields =  '__all__'
class InfoPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPerson
        fields =  '__all__'        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  '__all__'                      
        
    def to_representation(self, instance):
        representation = super(ProfileSerializer, self).to_representation(instance)
        representation['subscription'] = SubscriptionSerializer(instance.subscription_set.all(), many=True).data
       
        return representation    