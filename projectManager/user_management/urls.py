from django.urls import include, path
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'groups', api.GroupViewSet)
router.register(r'profile', api.ProfileViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('auth-profile',api.UserProfileViewSet.as_view()),
     path('user-profiles',api.UserProfilesViewSet.as_view()),
    path('', include(router.urls)),
]