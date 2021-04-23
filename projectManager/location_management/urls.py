from django.urls import include, path
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'region', api.RegionViewSet)
router.register(r'zone', api.ZoneViewSet)
router.register(r'wereda', api.WeredaViewSet)
router.register(r'city', api.CityViewSet)
router.register(r'sub-city', api.SubCityViewSet)
router.register(r'kebele', api.KebeleViewSet)
router.register(r'wereda-kebele', api.WeredaKebeleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]