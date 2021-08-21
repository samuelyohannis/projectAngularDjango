from django.urls import include, path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'notification', NotificationViewSet)

#router.register(r'all', api.ProjectList)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]