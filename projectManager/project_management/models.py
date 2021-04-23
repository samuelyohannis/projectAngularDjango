from django.db import models

# Create your models here.

from location_management.models import  *

from PIL import Image
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from resizeimage import resizeimage


class Project(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    img=models.ImageField(null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)    
class ZoneProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path) 
class CountryProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img = models.ImageField(null=True,upload_to='images/countryProject')
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True)  
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)

class RegionProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True,upload_to='images/countryProject')
    
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True)
    
    objects = models.Manager() # The default manager.
    # The Dahl-specific manager.  
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)
       
class WeredaProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True)
    wereda = models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path) 
class CityProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True) 
    img=models.ImageField(null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)
class SubCityProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True) 
    img=models.ImageField(null=True)
    sub_city = models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)                         
class KebeleProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date= models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True)
    kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)
class WeredaKebeleProject(models.Model):
    name = models.CharField(max_length=100)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date= models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True)
    wereda_kebele = models.ForeignKey(WeredaKebele,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)           
class CountryProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/countryProJect',null=True)
    file = models.FileField(upload_to = 'files/countryProJect',null=True)
    country_project = models.ForeignKey(CountryProject,on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True)  
class RegionProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/regionProJect',null=True)
    file = models.FileField(upload_to = 'files/regionProJect',null=True)
    region_project= models.ForeignKey(RegionProject,on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True) 
class ZoneProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/zoneProJect',null=True)
    file = models.FileField(upload_to = 'files/zoneProJect',null=True)
    zone_project = models.ForeignKey(ZoneProject,on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)  
class WeredaProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/weredaProJect',null=True)
    file = models.FileField(upload_to = 'files/weredaProJect',null=True)
    wereda_project = models.ForeignKey(WeredaProject,on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True) 
class CityProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/cityProJect',null=True)
    file = models.FileField(upload_to = 'files/cityProJect',null=True)
    city_project = models.ForeignKey(CityProject,on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True)  
class SubCityProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/cityProJect',null=True)
    file = models.FileField(upload_to = 'files/cityProJect',null=True)
    sub_city_project = models.ForeignKey(SubCityProject,on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True)    
class KebeleProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/kebeleProJect',null=True)
    file = models.FileField(upload_to = 'files/kebeleProJect',null=True)
    kebele_project = models.ForeignKey(KebeleProject,on_delete=models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True)    
class WeredaKebeleProjectFiles(models.Model):
    img = models.ImageField(upload_to = 'images/kebeleProJect',null=True)
    file = models.FileField(upload_to = 'files/kebeleProJect',null=True)
    wreda_kebele_project = models.ForeignKey(WeredaKebeleProject,on_delete = models.CASCADE,)
    date_modified = models.DateTimeField(auto_now=True)    