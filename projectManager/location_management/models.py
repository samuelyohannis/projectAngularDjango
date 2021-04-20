
# Create your models here.


# Create your models here.
from django.db import models
class Contenent(models.Model):
    name = models.CharField(max_length=1000)
    img= models.ImageField(upload_to='contenent_images',null=True) 
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True) 
class Country(models.Model):
    name = models.CharField(max_length=1000)
    img= models.ImageField(upload_to='country_images',null=True) 
    Contenent = models.ForeignKey(Contenent,on_delete=models.CASCADE,default=1)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)      
class Region(models.Model):
    name = models.CharField(max_length=1000)
    img= models.ImageField(upload_to='region_images',null=True) 
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True) 
class Zone(models.Model):
    name = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='zone_images',null=True) 
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)        
class Wereda(models.Model):
    name = models.CharField(max_length=1000)
    img= models.ImageField(upload_to='wereda_images',null=True) 
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
class City(models.Model):
    name = models.CharField(max_length=1000)
    img= models.ImageField(upload_to='city_images',null=True) 
    wereda = models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)       
class SubCity(models.Model):
    name = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='city_images',null=True) 
    wereda = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)          
class Kebele(models.Model):
    name = models.CharField(max_length=1000)
    img= models.ImageField(upload_to='kebele_images',null=True) 
    city =models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
class WeredaKebele(models.Model):
    name = models.CharField(max_length=1000)
    img= models.ImageField(upload_to='kebele_images',null=True) 
    city =models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)    