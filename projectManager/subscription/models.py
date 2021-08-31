from user_management.models import Profile
from django.db import models

# Create your models here.

class Subscription(models.Model):
    subscribed_resource = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
    
    