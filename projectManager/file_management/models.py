from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=1000)
    url = models.TextField() 
    views = models.IntegerField()
    date = models.DateTimeField(auto_now=True) 