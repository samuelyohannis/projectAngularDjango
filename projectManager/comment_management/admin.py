from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.
admin.site.register(RegionProjectComment)
admin.site.register(CityProjectComment)
admin.site.register(KebeleProjectComment)
admin.site.register(WeredaProjectComment)
admin.site.register(ZoneProjectComment)
admin.site.register(CountryProjectComment)