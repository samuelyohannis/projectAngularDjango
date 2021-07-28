from user_management.models import Profile
from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.TextField(max_length=10000)
    #profile= models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    date_created = models.DateField(auto_now=True)