from rest_framework import viewsets,permissions,generics
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from .models import *
from location_management.models import *
from django.shortcuts import get_object_or_404



pcv1 = [permissions.IsAuthenticated,]
pcv2 = [permissions.AllowAny,]
prcv = [MultiPartParser,FormParser,JSONParser,]

# if (False):
#     from constants import *  
class ViewSetCommonForAll(viewsets.ModelViewSet):
    parser_classes = prcv
    
class ProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes= pcv2  
class RegionProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegionProject.objects.all()
    serializer_class = RegionProjectSerializer
    permission_classes= pcv2 
    
class ZoneProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegionProject.objects.all()
    serializer_class = RegionProjectSerializer
    permission_classes= pcv2 
    
class WeredaProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ZoneProject.objects.all()
    serializer_class = ZoneProjectSerializer
    permission_classes= pcv2 
    
class CityProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CityProject.objects.all()
    serializer_class = CityProjectSerializer
    permission_classes= pcv2 
    
    
class KebeleProjectViewSet(ViewSetCommonForAll):

    queryset = KebeleProject.objects.all()
    serializer_class = KebeleProjectSerializer
    permission_classes= pcv2                
class UserRegionProject(ViewSetCommonForAll):
    queryset = RegionProject.objects.all()
    serializer_class = RegionProjectSerializer 
    def get_queryset(self):
            return RegionProject.objects.filter(region=self.request.user.profile.region)
class UserZoneProject(ViewSetCommonForAll):
    queryset = ZoneProject.objects.all()    
    serializer_class = ZoneProjectSerializer 
    def get_queryset(self):
            return ZoneProject.objects.filter(region=self.request.user.profile.region)   
        
        
class UserWeredaProject(ViewSetCommonForAll):
    queryset = WeredaProject.objects.all()
    serializer_class = WeredaProjectSerializer 
    def get_queryset(self):
            return WeredaProject.objects.filter(region=self.request.user.profile.region)

class UserCityProject(ViewSetCommonForAll):
    queryset = CityProject.objects.all()
    serializer_class = CityProjectSerializer 
    def get_queryset(self):
            return CityProject.objects.filter(region=self.request.user.profile.region)
        
class UserKebeleProject(ViewSetCommonForAll):
    queryset = KebeleProject.objects.all()
    serializer_class = KebeleProjectSerializer 
    def get_queryset(self):
            return KebeleProject.objects.filter(region=self.request.user.profile.region) 
        
''' class UserRegionProjects(ViewSetCommonForAll):
    
    serializer_class = RegionProjectSerializer 
    def get_queryset(self):
            return RegionProject.objects.filter(region=self.request.user.profile.region)     '''                            
''' class ContenentViewSet(ViewSetCommonForAll):
  
    queryset = Contenent.objects.all()
    serializer_class = ContenentSerializer
class CountryViewSet(ViewSetCommonForAll):
  
    queryset = Country.objects.all()
    serializer_class = CountrySerializer  '''       