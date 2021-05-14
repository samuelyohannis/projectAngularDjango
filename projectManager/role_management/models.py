from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.TextField(max_length=10000)
    date_created = models.DateField(auto_now=True)