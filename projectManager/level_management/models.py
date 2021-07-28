
from user_management.models import Profile
from django.db import models


# Create your models here.
class Level(models.Model):
    name = models.CharField(max_length=500)
    #profile= models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now=True)      
     