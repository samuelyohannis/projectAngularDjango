from list_management.views import listFactory
from .models import *
from .serializers import *
from crud_management.views import crudFactory
from detail_management.views import detailFactory

from django.urls import include, path
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'project', api.ProjectViewSet)
router.register(r'country-project', api.CountryProjectViewSet)
router.register(r'region-project', api.RegionProjectViewSet)
router.register(r'zone-project', api.ZoneProjectViewSet)
router.register(r'wereda-project', api.WeredaProjectViewSet)
router.register(r'city-project', api.CityProjectViewSet)
router.register(r'kebele-project', api.KebeleProjectViewSet)
router.register(r'user-region-project', api.UserRegionProject)
router.register(r'user-zone-project', api.UserZoneProject)
router.register(r'user-wereda-project', api.UserWeredaProject)
router.register(r'user-city-project', api.UserCityProject)
router.register(r'user-kebele-project', api.UserKebeleProject)
#router.register(r'all', api.ProjectList)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path('all', api.ProjectList),
               path('all-user', api.UserProjectList),
               path('country/report/',crudFactory().as_view(CountryProjectReportSerializer,CountryProjectReport)),
               path('country/report/<int:pk>', detailFactory().as_view(CountryProjectReportSerializer,CountryProjectReport)),
               path('region/report',crudFactory().as_view(RegionProjectReportSerializer,RegionProjectReport)),
               path('region/report/<int:pk>/', detailFactory().as_view(RegionProjectReportSerializer,RegionProjectReport)),
               path('zone/report',crudFactory().as_view(ZoneProjectReportSerializer,ZoneProjectReport)),
               path('zone/report/<int:pk>/', detailFactory().as_view(ZoneProjectReportSerializer,ZoneProjectReport)),
               path('wereda/report',crudFactory().as_view(WeredaProjectReportSerializer,WeredaProjectReport)),
               path('wereda/report/<int:pk>/', detailFactory().as_view(WeredaProjectReportSerializer,WeredaProjectReport)),
               path('user/reports/',api.UserProjectReportList),
              
               path('', include(router.urls))
             ]