from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .serializers import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from .models import *
import json
from itertools import chain
from operator import itemgetter, attrgetter
from rest_framework.decorators import api_view
from location_management.models import *
from django.shortcuts import get_object_or_404
# Create your views here.
pcv1 = [permissions.IsAuthenticated,]
pcv2 = [permissions.AllowAny,]
prcv = [MultiPartParser,FormParser,JSONParser,]



class NotificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Notifications to be viewed or edited.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]