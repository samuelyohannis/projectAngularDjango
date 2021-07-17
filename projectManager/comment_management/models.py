from user_management.models import Profile
from django.db import models

# Create your models here.

from project_management.models import  *
from level_management.models import  *
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from resizeimage import resizeimage

class Comment(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
class ProjectComment(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)
    level = models.OneToOneField(Level, on_delete=models.SET_NULL ,null=True)
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
    
class CountryProjectComment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)
    level = models.IntegerField(null=True,default=1)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(CountryProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)  
    
    
class RegionProjectComment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)
    level = models.IntegerField(null=True,default=2)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(RegionProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)  
    
class ZoneProjectComment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)
    level = models.IntegerField(null=True,default=3)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(ZoneProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)          
    
    
class WeredaProjectComment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)
    level = models.IntegerField(null=True,default=4)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(WeredaProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)      
    
class CityProjectComment(models.Model):
    level = models.IntegerField(null=True,default=5)
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(CityProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)      
    
    
class SubCityProjectComment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)
    level = models.IntegerField(null=True,default=6)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(SubCityProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)      
    
class KebeleProjectComment(models.Model):
    profile= models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True) 
    level = models.IntegerField(null=True,default=7)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(KebeleProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)  
    
class WeredaKebeleProjectComment(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL ,null=True)  
    level = models.IntegerField(null=True,default=8)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(WeredaKebeleProject,on_delete=models.SET_NULL,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)          
    
def nullify():
    pass    