from level_management.models import Level
from report_management.models import Report
from progress_management.models import Progress
from user_management.models import Profile
from django.db import models

# Create your models here.

from location_management.models import  *

from PIL import Image
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from resizeimage import resizeimage

class ProjectCategory(models.Model):
    name = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
class Project(models.Model):
    name = models.CharField(max_length=100,null=True)
    catagory =  models.ForeignKey(ProjectCategory,on_delete=models.SET_NULL,null=True)
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
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True,upload_to='images/weredaProject',default='images/project-logo.png')
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE,null=True)
    reported = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
       
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path) 
class CountryProject(models.Model):
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img = models.ImageField(null=True,upload_to='images/countryProject',default='images/project-logo.png')
    country = models.ForeignKey(Country,on_delete=models.CASCADE,default=1)
    reported = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)  
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)

class RegionProject(models.Model):
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True,upload_to='images/regionProject',default='images/regionProject/regions.jpg')
    
    region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True)
    reported = models.BooleanField(default=False)
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
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(upload_to='images/weredaProject',null=True,default='images/project-logo.png')
    wereda = models.ForeignKey(Wereda,on_delete=models.CASCADE,null=True)
    reported = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True) 
    
    def save(self,*args,**kwargs):
    
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path) 
class CityProject(models.Model):
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True) 
    img=models.ImageField(null=True,upload_to='images/cityProject',default='images/project-logo.png')
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    reported = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width) 
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)
class SubCityProject(models.Model):
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    desc = models.TextField(null=True) 
    img=models.ImageField(upload_to='images/subCityProject',null=True,default='images/project-logo.png')
    sub_city = models.ForeignKey(SubCity,on_delete=models.CASCADE,null=True)
    reported = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)                         
class KebeleProject(models.Model):
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date= models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(upload_to='images/kebeleProject',null=True,default='images/project-logo.png')
    kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True)
    reported = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)
class WeredaKebeleProject(models.Model):
    name = models.CharField(max_length=100,null=True)
    catagory =  models.IntegerField(null=True)
    completion = models.IntegerField(default=0)
    bujdet = models.IntegerField(default=0)
    level= models.IntegerField(null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    start_date = models.DateField(null=True)
    end_date= models.DateField(null=True)
    desc = models.TextField(null=True)
    img=models.ImageField(null=True,upload_to='images/weredaKebeleProject',default='images/project-logo.png')
    wereda_kebele = models.ForeignKey(WeredaKebele,on_delete=models.CASCADE,null=True)
    reported = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img  = Image.open(self.img.path)
        newWidth=500
        newHeight =int(img.height*newWidth/img.width)
        img1 = resizeimage.resize_thumbnail(img, [newWidth, newHeight])
        img1.save(self.img.path)           
class CountryProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/countryProJect',null=True)
    project = models.ForeignKey(CountryProject,on_delete=models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)  
class RegionProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/regionProJect',null=True)
    project= models.ForeignKey(RegionProject,on_delete=models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True) 
class ZoneProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/zoneProJect',null=True)
    project = models.ForeignKey(ZoneProject,on_delete=models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)  
class WeredaProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/weredaProJect',null=True )
    project = models.ForeignKey(WeredaProject,on_delete=models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True) 
class CityProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/cityProJect',null=True )
    project = models.ForeignKey(CityProject,on_delete=models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)  
class SubCityProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/subCityProJect',null=True)
    project = models.ForeignKey(SubCityProject,on_delete=models.CASCADE, null=True )
    date_modified = models.DateTimeField(auto_now=True)    
class KebeleProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/kebeleProJect',null=True)
    project = models.ForeignKey(KebeleProject,on_delete=models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)    
class WeredaKebeleProjectFile(models.Model):
    file = models.FileField(upload_to = 'files/weredaKebeleProJect',null=True)
    project = models.ForeignKey(WeredaKebeleProject,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True) 
 
    
class CountryProjectProgress(models.Model): 
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    project = models.ForeignKey(CountryProject,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)    
class RegionProjectProgress(models.Model):
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    project = models.ForeignKey(RegionProject,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)
class ZoneProjectProgress(models.Model):
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    project = models.ForeignKey(ZoneProject,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)
class WeredaProjectProgress(models.Model):
    project = models.ForeignKey(WeredaProject,on_delete = models.CASCADE,null=True)
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True) 
class CityProjectProgress(models.Model):
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    project = models.ForeignKey(CityProject,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)
class SubCityProjectProgress(models.Model):
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    project = models.ForeignKey(SubCityProject,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)
class KebeleProjectProgress(models.Model):
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    project = models.ForeignKey(KebeleProject,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)
class WeredaKebeleProjectProgress(models.Model):
    progress = models.OneToOneField(Progress,on_delete = models.CASCADE,null=True)
    project = models.ForeignKey(WeredaKebeleProject,on_delete = models.CASCADE,null=True)
    date_modified = models.DateTimeField(auto_now=True)                                
    
    
class CountryProjectReport(models.Model): 
    
    project = models.ForeignKey(CountryProject,on_delete = models.CASCADE,null=True )
    worklevel=models.IntegerField(default=9)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
     
class RegionProjectReport(models.Model):
   
    worklevel=models.IntegerField(default=9)
    project = models.ForeignKey(RegionProject,on_delete = models.CASCADE,null=True,)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    percentage = models.IntegerField(default=0)
   
    date = models.DateTimeField(auto_now=True)
class ZoneProjectReport(models.Model):
    worklevel=models.IntegerField(default=9)
    project = models.ForeignKey(ZoneProject,on_delete = models.CASCADE,null=True,)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
class WeredaProjectReport(models.Model):
    worklevel=models.IntegerField(default=9)
    project = models.ForeignKey(WeredaProject,on_delete = models.CASCADE,null=True,)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True) 
class CityProjectReport(models.Model):
    worklevel=models.IntegerField(default=9)
    project = models.ForeignKey(CityProject,on_delete = models.CASCADE,null=True,)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
class SubCityProjectReport(models.Model):
    worklevel=models.IntegerField(default=9)
    project = models.ForeignKey(SubCityProject,on_delete = models.CASCADE,null=True,)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
class KebeleProjectReport(models.Model):
    worklevel=models.IntegerField(default=9)
    project = models.ForeignKey(KebeleProject,on_delete = models.CASCADE,null=True,)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
class WeredaKebeleProjectReport(models.Model):
    worklevel=models.IntegerField(default=9)
    project = models.ForeignKey(WeredaKebeleProject,on_delete = models.CASCADE,null=True,)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,default=1)
    name = models.CharField(max_length=1000,null=True)
    desc =models.TextField(default='report')
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)          
class CityProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/cityProJect/report/',null=True)
    report = models.ForeignKey(CityProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)        
class CountryProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/countryProJect/report/',null=True)
    report = models.ForeignKey(CountryProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)       
class RegionProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/regionProJect/report/',null=True)
    report = models.ForeignKey(RegionProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)   
    
class ZoneProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/zoneProJect/report/',null=True)
    report = models.ForeignKey(ZoneProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)   
class WeredaProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/weredaProJect/report/',null=True)
    report = models.ForeignKey(WeredaProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)
class SubCityProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/subCityProJect/report/',null=True)
    report = models.ForeignKey(SubCityProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)   
class KebeleProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/kebeleProJect/report/',null=True)
    report = models.ForeignKey(KebeleProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)   
class WeredaKebeleProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/weredaKebeleProJect/report/',null=True)
    report = models.ForeignKey(WeredaKebeleProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)   
    
    
class CountryProjectReportFile(models.Model):
    file = models.FileField(upload_to = 'files/countryProJect/report/',null=True)
    report = models.ForeignKey(CountryProjectReport,on_delete = models.CASCADE,null=True )
    date_modified = models.DateTimeField(auto_now=True)                              