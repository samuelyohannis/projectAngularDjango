from file_management.models import File
from django.db import models

# Create your models here.
from PIL import Image
from django.utils.timezone import now
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from resizeimage import resizeimage


class Progress(models.Model):
    name = models.CharField(max_length=1000)
    percentage = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    
class ProgressFile(File):
     progress = models.ForeignKey(Progress,on_delete=models.SET_NULL,null=True)
    