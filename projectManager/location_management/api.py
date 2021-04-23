from rest_framework import viewsets,permissions,generics
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from .models import *
from django.shortcuts import get_object_or_404



pcv1 = [permissions.IsAuthenticated,]
pcv2 = [permissions.AllowAny,]
prcv = [MultiPartParser,FormParser,JSONParser,]

# if (False):
#     from constants import *  
class ViewSetCommonForAll(viewsets.ModelViewSet):
    parser_classes = prcv
    

class RegionViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes= pcv1
class ZoneViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes= pcv1
class WeredaViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Wereda.objects.all()
    serializer_class = WeredaSerializer
    permission_classes= pcv1      
class CityViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes= pcv1    
class SubCityViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SubCity.objects.all()
    serializer_class = SubCitySerializer
    permission_classes= pcv1    
class KebeleViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Kebele.objects.all()
    serializer_class = KebeleSerializer
    permission_classes= pcv1    
class WeredaKebeleViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WeredaKebele.objects.all()
    serializer_class = WeredaKebeleSerializer
    permission_classes= pcv1    