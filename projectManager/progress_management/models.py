from django.db import models

# Create your models here.
from PIL import Image
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from resizeimage import resizeimage


class Progress(models.Model):
    name = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    
class ProgressFile(models.Model):
    name = models.CharField(max_length=1000)
    url = models.TextField() 
    progress = models.ForeignKey(Progress,on_delete=models.SET_NULL,null=True)
    views = models.IntegerField()
    date = models.DateTimeField(auto_now=True)    