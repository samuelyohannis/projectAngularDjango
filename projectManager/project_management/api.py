from rest_framework import viewsets,permissions,generics
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from .models import *
from itertools import chain
from operator import itemgetter, attrgetter
from rest_framework.decorators import api_view
from location_management.models import *
from django.shortcuts import get_object_or_404

pcv1 = [permissions.IsAuthenticated,]
pcv2 = [permissions.AllowAny,]
prcv = [MultiPartParser,FormParser,JSONParser,]

# if (False):
#     from constants import *  
SL =['CountryProjectSerializer','RegionProjectSerializer','ZoneProjectSerializer','WeredaProjectSerializer','CityProjectSerializer','KebeleProjectSerializer','SubCityProjectSerializer','WeredaKebeleProjectSerializer']
ML =['CountryProject','RegionProject','ZoneProject','WeredaProject','CityProject','KebeleProject','SubCityProject','WeredaKebeleProject']
SL1 =['CountryProjectReportSerializer','RegionProjectReportSerializer','ZoneProjectReportSerializer','WeredaProjectReportSerializer','CityProjectReportSerializer','KebeleProjectReportSerializer','SubCityProjectReportSerializer','WeredaKebeleProjectReportSerializer']
ML1 =['CountryProjectReport','RegionProjectReport','ZoneProjectReport','WeredaProjectReport','CityProjectReport','KebeleProjectReport','SubCityProjectReport','WeredaKebeleProjectReport']
gb =  globals()
dc1 = globals()['DynamicSerializerClass']
class ViewSetCommonForAll(viewsets.ModelViewSet):
    parser_classes = prcv
    
@api_view(['GET'])
def UserProjectList(request):
     
       project_list =[]
       for x in range(len(ML)):
         if(x==0):
             project_list = project_list + gb[SL[x]](gb[ML[x]].objects.filter(country=request.user.profile.country),many=True).data   
         if(x==1):
             project_list = project_list + gb[SL[x]](gb[ML[x]].objects.filter(region=request.user.profile.region),many=True).data 
         if(x==3):
             project_list = project_list + gb[SL[x]](gb[ML[x]].objects.filter(wereda=request.user.profile.wereda),many=True).data 
         
         if(x==2):
              project_list = project_list + gb[SL[x]](gb[ML[x]].objects.filter(zone=request.user.profile.zone),many=True).data 
         
         if(x==4):
              project_list = project_list + gb[SL[x]](gb[ML[x]].objects.filter(city=request.user.profile.city),many=True).data 
         
         if(x==5):
              project_list = project_list + gb[SL[x]](gb[ML[x]].objects.filter(kebele=request.user.profile.kebele),many=True).data 
         ''' if(x==0):
              project_list = project_list + gb[SL[x]](gb[ML[x]].objects.filter(country=request.user.profile.country),many=True).data 
          '''
      
       #sorted(problem_list, key=attrgetter("date"))
       all_projects = sorted(project_list, key=itemgetter("id"))
       return Response(all_projects)     
@api_view(['GET'])
def ProjectList(request):
      
       project_list =[]
       for x in range(len(ML)):
          project_list = project_list + gb[SL[x]](gb[ML[x]].objects.all(),many=True).data 
      
       #sorted(problem_list, key=attrgetter("date"))
       
       all_projects = sorted(project_list, key=itemgetter("date"))
       return Response(all_projects)    
class ProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes= pcv2
class CountryProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CountryProject.objects.all()
    serializer_class = CountryProjectSerializer
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
    queryset = ZoneProject.objects.all()
    serializer_class = ZoneProjectSerializer
    permission_classes= pcv2 
    
class WeredaProjectViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WeredaProject.objects.all()
    serializer_class = WeredaProjectSerializer
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
    
@api_view(['GET'])
def UserProjectReportList(request):
    
       project_report_list =[]
       for x in range(len(ML1)):
              project_report_list =  project_report_list + gb[SL1[x]](gb[ML1[x]].objects.filter(profile=request.user.profile.id),many=True).data   
        
      
       #sorted(problem_list, key=attrgetter("date"))
       all_project_report_list = sorted( project_report_list, key=itemgetter("id"))
       return Response(all_project_report_list)          