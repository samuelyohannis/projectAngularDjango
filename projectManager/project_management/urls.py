from update_management.views import updateFactory
from crud_management.views import crudWithRelatedFileFactory
from create_management.views import createWithRelatedFileFactory
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
router.register(r'sub-city-project', api.SubCityProjectViewSet)
router.register(r'kebele-project', api.KebeleProjectViewSet)
router.register(r'wereda-kebele-project', api.WeredaKebeleProjectViewSet)
router.register(r'user-region-project', api.UserRegionProject)
router.register(r'user-zone-project', api.UserZoneProject)
router.register(r'user-wereda-project', api.UserWeredaProject)
router.register(r'user-city-project', api.UserCityProject)
router.register(r'user-kebele-project', api.UserKebeleProject)
router.register(r'country/report',api.dynamicViewSetWithRelatedDataFactory(CountryProjectReportSerializer,CountryProjectReportFileSerializer,CountryProjectReport,CountryProjectReportFile,'countryprojectreportfile'))
router.register(r'region/report',api.dynamicViewSetWithRelatedDataFactory(RegionProjectReportSerializer,RegionProjectReportFileSerializer,RegionProjectReport,RegionProjectReportFile,'regionprojectreportfile'))
router.register(r'zone/report',api.dynamicViewSetWithRelatedDataFactory(ZoneProjectReportSerializer,ZoneProjectReportFileSerializer,ZoneProjectReport,ZoneProjectReportFile,'zoneprojectreportfile'))
router.register(r'wereda/report',api.dynamicViewSetWithRelatedDataFactory(WeredaProjectReportSerializer,WeredaProjectReportFileSerializer,WeredaProjectReport,WeredaProjectReportFile,'weredaprojectreportfile'))
router.register(r'city/report',api.dynamicViewSetWithRelatedDataFactory(CityProjectReportSerializer,CityProjectReportFileSerializer,CityProjectReport,CityProjectReportFile,'cityprojectreportfile'))
router.register(r'sub-city/report',api.dynamicViewSetWithRelatedDataFactory(SubCityProjectReportSerializer,SubCityProjectReportFileSerializer,SubCityProjectReport,SubCityProjectReportFile,'subcityprojectreportfile'))
router.register(r'kebele/report',api.dynamicViewSetWithRelatedDataFactory(KebeleProjectReportSerializer,KebeleProjectReportFileSerializer,KebeleProjectReport,KebeleProjectReportFile,'kebeleprojectreportfile'))
router.register(r'wereda-kebele/report',api.dynamicViewSetWithRelatedDataFactory(WeredaKebeleProjectReportSerializer,WeredaKebeleProjectReportFileSerializer,WeredaKebeleProjectReport,WeredaKebeleProjectReportFile,'weredakebeleprojectreportfile'))

""" router.register(r'country/report',api.CountryProjectReport)
router.register(r'region/report',api.RegionProjectReport)
router.register(r'zone/report',api.ZoneProjectReport)
router.register(r'wereda/report',api.WeredaProjectReport)
router.register(r'city/report',api.CityProjectReport)
router.register(r'sub-city/report',api.SubCityProjectReport)
router.register(r'kebele/report',api.KebeleProjectReport)
router.register(r'wereda-kebele/report',api.WeredaKebeleProjectReport) """
#router.register(r'all', api.ProjectList)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path('all', api.ProjectList),
               path('all-user', api.UserProjectList),
               
               
               path('user/reports/',api.UserProjectReportList),
               path('user/not-reported/',api.NotReportedUserProjectList),
               path('user/authorized/',api.AuthorizedUserProjectList),
               path('rek',createWithRelatedFileFactory().as_view(CountryProjectSerializer,CountryProjectFileSerializer,CountryProject,CountryProjectFile,'countryprojectfile')),
             
              
               path('', include(router.urls))
             ]



""" path('country/report/<int:pk>/', updateFactory().as_view(CountryProjectReportSerializer,CountryProjectReport)),
               path('country/report/<int:pk>', detailFactory().as_view(CountryProjectReportSerializer,CountryProjectReport)),
               path('country/report/',crudWithRelatedFileFactory().as_view(CountryProjectReportSerializer,CountryProjectReportFileSerializer,CountryProjectReport,CountryProjectReportFile,'countryprojectreportfile')), """
               
               
               