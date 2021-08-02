from django.db.models.fields.related import OneToOneField
from file_management.models import File
from django.db import models

# Create your models here.
from PIL import Image
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from resizeimage import resizeimage


class Report(models.Model):
    name = models.CharField(max_length=1000)
    desc =models.TextField()
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    
class ReportFile(models.Model):
     file= OneToOneField(File,on_delete= models.SET_NULL,null=True)
     report = models.ForeignKey(Report,on_delete=models.SET_NULL,null=True)
        