from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

admin.site.register(Region)
admin.site.register(City)
admin.site.register(Kebele)
admin.site.register(Wereda)
admin.site.register(Zone)
admin.site.register(Contenent)
admin.site.register(Country)