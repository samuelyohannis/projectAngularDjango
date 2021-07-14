from django.urls import include, path
from rest_framework import routers
from .views import Update
from project_management.serializers import RegionProjectSerializer
from project_management.models import RegionProject

urlpatterns = [
  path('test/<int:pk>/', Update.as_view(RegionProjectSerializer,RegionProject)),
]
