from django.urls import include, path
from rest_framework import routers
from .views import Create
from project_management.serializers import RegionProjectSerializer
from project_management.models import RegionProject

urlpatterns = [
  path('allevermm', Create.as_view(RegionProjectSerializer,RegionProject)),
]
