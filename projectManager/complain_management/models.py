from file_management.models import File
from django.db import models
from project_management.models import *
# Create your models here.
class ComplainCategory(models.Model):
    name = models.TextField(null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True) 
class Complain(models.Model):
    title = models.TextField(null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)  
    category = models.ForeignKey(ComplainCategory,on_delete=models.SET_NULL,null=True)
 

''' class ProjectComplain(Complain):
    
   project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True) '''    
''' class CountryProjectComplain(Complain):
    project = models.ForeignKey(CountryProject,on_delete=models.CASCADE,null=True)
    
class RegionProjectComplain(Complain):

    project = models.ForeignKey(RegionProject,on_delete=models.CASCADE,null=True)     
class ZoneProjectComplain(Complain):

    project = models.ForeignKey(ZoneProject,on_delete=models.CASCADE,null=True)        
class WeredaProjectComplain(Complain):

    project = models.ForeignKey(WeredaProject,on_delete=models.CASCADE,null=True)    
class CityProjectComplain(Complain):

    project = models.ForeignKey(CityProject,on_delete=models.CASCADE,null=True)    
class SubCityProjectComplain(Complain):

    project = models.ForeignKey(SubCityProject,on_delete=models.CASCADE,null=True)    
class KebeleProjectComplain(Complain):

    project = models.ForeignKey(KebeleProject,on_delete=models.CASCADE,null=True)  
class WeredaKebeleProjectComplain(Complain):

    project = models.ForeignKey(WeredaKebeleProject,on_delete=models.CASCADE,null=True)    '''   
    
    
''' class CountryProjectComplainFile(File):
     complain = models.ForeignKey(CountryProjectComplain,on_delete=models.CASCADE,null=True)     
     
class RegionProjectComplainFile(File):
     complain = models.ForeignKey(RegionProjectComplain,on_delete=models.CASCADE,null=True)    
class ZoneProjectComplainFile(File):
     complain = models.ForeignKey(ZoneProjectComplain,on_delete=models.CASCADE,null=True)  
     
class WeredaProjectComplainFile(File):
     complain = models.ForeignKey(WeredaProjectComplain,on_delete=models.CASCADE,null=True) 
class CityProjectComplainFile(File):
     complain = models.ForeignKey(CityProjectComplain,on_delete=models.CASCADE,null=True) 
class KebeleProjectComplainFile(File):
     complain = models.ForeignKey(KebeleProjectComplain,on_delete=models.CASCADE,null=True) 
class SubCityProjectComplainFile(File):
     complain = models.ForeignKey(SubCityProjectComplain,on_delete=models.CASCADE,null=True) 
     
class WeredaKebeleProjectComplainFile(File):
     complain = models.ForeignKey(WeredaKebeleProjectComplain,on_delete=models.CASCADE,null=True)                           '''