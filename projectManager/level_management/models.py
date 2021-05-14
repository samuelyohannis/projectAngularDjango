from django.db import models

# Create your models here.
class Level(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)      