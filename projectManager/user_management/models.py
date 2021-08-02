

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from location_management.models import *
    
    
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
    
# Create your models here.                   

class Role(models.Model) :
    name=  models.CharField(max_length=500)  
    date = models.DateTimeField(auto_now=True) 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    country = models.ForeignKey(Country,on_delete=models.CASCADE,default=1)
    bio = models.TextField(max_length=500, blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,null=True)
    wereda =  models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    city =  models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    sub_city =  models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    kebele =  models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True)
    wereda_kebele =  models.ForeignKey(WeredaKebele,on_delete=models.CASCADE,null=True)
    worklevel=models.IntegerField(null=True)
    role = models.IntegerField(null=True)
    experiance =  models.TextField(null=True)
   
    img = models.ImageField(upload_to='profile/images',default='profile/images/avatar.jpg',null=True)
    date = models.DateTimeField(auto_now=True)      
   
    """   def get_absolute_url(self):
        return reverse('profile-create') """
class ProfileEducation(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    education = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)        
class ProfileSkill(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    skills = models.TextField()
    date = models.DateTimeField(auto_now=True)   
class ProfileImage(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    img = models.ImageField(upload_to='images1',null=True)
    date = models.DateTimeField(auto_now=True)    
class Contact(models.Model):
   
    address = models.CharField(max_length=500)
    location = models.TextField()
    date = models.DateTimeField(auto_now=True)
class ContactEmail(models.Model):
    contact= models.ForeignKey(Contact,on_delete=models.CASCADE,null=True)
    email= models.EmailField(max_length=500)
    date = models.DateTimeField(auto_now=True)
class ContactPhone(models.Model):
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE,null=True) 
    phone = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)   
class About(models.Model):
    work = models.CharField(max_length=500)
    education = models.TextField(null=True)
    contact = models.OneToOneField(Contact,on_delete=models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)    
class CustomGroup(models.Model):
     user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
     group = models.TextField(null=True)
     date = models.DateTimeField(auto_now=True) 