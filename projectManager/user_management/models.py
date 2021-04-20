

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ..location_management.models import *
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,null=True)
    wereda =  models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    city =  models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    sub_city =  models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    kebele =  models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True)
    wereda_kebele =  models.ForeignKey(WeredaKebele,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True) 
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000, blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,null=True)
    wereda =  models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    city =  models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    sub_city =  models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    kebele =  models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True)
    wereda_kebele =  models.ForeignKey(WeredaKebele,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True) 
class InfoPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000, blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,null=True)
    wereda =  models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    city =  models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    sub_city =  models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    kebele =  models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True)
    wereda_kebele =  models.ForeignKey(WeredaKebele,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True) 
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000, blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,null=True)
    wereda =  models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    city =  models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    sub_city =  models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    kebele =  models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True)
    wereda_kebele =  models.ForeignKey(WeredaKebele,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True)         