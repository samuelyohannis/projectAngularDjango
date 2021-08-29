from user_management.models import Profile
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class chat(models.Model):
    pass
class Notification(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    is_viewed = models.BooleanField(default=False)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)