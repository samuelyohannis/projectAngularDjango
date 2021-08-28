from django.urls import re_path,path
from . import consumers

urlpatterns=[
     
     re_path(r'ws/notification/(?P<group_name>\w+)/$', consumers.NotificationConsumer.as_asgi()),
     re_path(r'ws/country/project/notification/(?P<group_name>\w+)/$', consumers.ProjectNotification.as_asgi())
]