from user_management.models import Profile
from django.db import models

# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=100)
    is_viewed = models.BooleanField(default=False)
    desc = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)