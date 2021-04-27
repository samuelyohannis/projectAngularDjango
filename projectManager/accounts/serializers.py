from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
import json
import ast
# User Serializer
class UserSerializer1(serializers.ModelSerializer):
  class Meta:
    model = User
    fields ='__all__'

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password','groups')
    extra_kwargs = {'password': {'write_only': True},}
  
  def Convert(self,string1): 
      li = list(string1.split(" ")) 
      return li    

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    # group1 = Group.objects.get(name=list(validated_data['groups'])[0]) 
   # group2 = Group.objects.get(name=list(validated_data['groups'])[1]) 
    #user.groups.add([validated_data['groups']])
    # groups_data = validated_data.pop('groups')
    # for group_data in groups_data:
    #     # Group.objects.create(user=user, **group_data)
    #     user.groups.add(group_data)
    # def Convert(string): 
    # li = list(string.split(" ")) 
    # return li 
   
    user.groups.add(validated_data['groups'][0],validated_data['groups'][1])
    #user.groups.add(validated_data['groups'][1])
    #user.groups.set([validated_data['groups'][0]])
   # user.groups.set(validated_data['groups'])
    #user.groups.set(list(validated_data['level']))
    # user.groups.add(validated_data['groups'][1])
    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")