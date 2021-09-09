from django.urls import re_path,path
from . import consumers

urlpatterns=[
     
     re_path(r'ws/notification/(?P<group_name>\w+)/(?P<profile_id>\w+)/$', consumers.NotificationConsumer1.as_asgi()),
     re_path(r'ws/country/project/notification/(?P<group_name>\w+)/(?P<profile_id>\w+)/$', consumers.ProjectNotification.as_asgi()),
    
]