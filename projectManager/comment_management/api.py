from user_management.models import Profile
from user_management.serializers import ProfileSerializer
from rest_framework import viewsets,permissions,generics
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from .models import *
from itertools import chain
from operator import itemgetter, attrgetter, xor
from rest_framework.decorators import api_view
from project_management.models import *
from django.shortcuts import get_object_or_404



pcv1 = [permissions.IsAuthenticated,]
pcv2 = [permissions.AllowAny,]
prcv = [MultiPartParser,FormParser,JSONParser,]

# if (False):
#     from constants import *  Comment
SL =['CountryProjectCommentSerializer','RegionProjectCommentSerializer','ZoneProjectCommentSerializer','WeredaProjectCommentSerializer','CityProjectCommentSerializer','KebeleProjectCommentSerializer','SubCityProjectCommentSerializer','WeredaKebeleProjectCommentSerializer']
ML =['CountryProjectComment','RegionProjectComment','ZoneProjectComment','WeredaProjectComment','CityProjectComment','KebeleProjectComment','SubCityProjectComment','WeredaKebeleProjectComment']
gb =  globals()
dc1 = globals()['DynamicSerializerClass']
class ViewSetCommonForAll(viewsets.ModelViewSet):
    parser_classes = prcv
    
@api_view(['GET'])
def UserProjectCommentList(request):
     
       project_comment_list =[]
       
       for x in range(len(ML)):
         
            project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(profile=request.user.profile.id),many=True).data 
       all_project_comments = sorted(project_comment_list, key=itemgetter("date"))
       return Response(all_project_comments) 
      
'''  for x in range(len(ML)):
         if(x==1):
             project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(profile=request.user.profile.id),many=True).data 
         if(x==3):
             project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(profile=request.user.profile.id),many=True).data 
         
         if(x==2):
              project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(profile=request.user.profile.id),many=True).data 
         
         if(x==4):
              project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(profile=request.user.profile.id),many=True).data 
         
         if(x==5):
              project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(profile=request.user.profile.id),many=True).data  '''
         
      
       #sorted(problem_list, key=attrgetter("date"))
       
@api_view(['GET','POST'])
def UserProjectCommentList1(request):
    if request.method=='POST':
       project_comment_list = []
       project_comment_profiles_dict={}
       project_comment_profiles=[]
       project_comment_profile_ids=[]
       for x in range(len(ML)):
         for y in range(len(request.POST.getlist('level'))):
                 project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(level=request.POST.getlist('level')[y],project=request.POST.getlist('project')[y]),many=True).data 
         '''if(x==1):
            for y in range(len(request.POST.getlist('level'))):
             project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(level=request.POST.getlist('level')[y],project=request.POST.getlist('project')[y]),many=True).data 
         if(x==3):
          for y in range(len(request.POST.getlist('level'))):
             project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(level=request.POST.getlist('level')[y],project=request.POST.getlist('project')[y]),many=True).data 
         
         if(x==2):
            for y in range(len(request.POST.getlist('level'))): 
              project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(level=request.POST.getlist('level')[y],project=request.POST.getlist('project')[y]),many=True).data 
         
         if(x==4):
            for y in range(len(request.POST.getlist('level'))): 
              project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(level=request.POST.getlist('level')[y],project=request.POST.getlist('project')[y]),many=True).data 
         
         if(x==5):
             for y in range(len(request.POST.getlist('level'))):
              project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.filter(level=request.POST.getlist('level')[y],project=request.POST.getlist('project')[y]),many=True).data 
         '''
       for x1 in range(len(project_comment_list)):
           
           if project_comment_list[x1]['profile'] not in  project_comment_profile_ids:
            project_comment_profiles =project_comment_profiles + ProfileSerializer(Profile.objects.filter(id=project_comment_list[x1]["profile"]),many=True).data
           project_comment_profile_ids.append(project_comment_list[x1]['profile'])
       for x1 in range(len(project_comment_profiles)):
           
           project_comment_profiles_dict[project_comment_profiles[x1]['id']] =  project_comment_profiles[x1]
       #sorted(problem_list, key=attrgetter("date"))
       all_project_comments = sorted(project_comment_list, key=itemgetter("project"))
       return Response({"comments":all_project_comments,"profiles":project_comment_profiles_dict})
   
@api_view(['POST'])
def RelatedListProvider(request,*args):
    if request.method=='POST':
       list1 = []
       profiles_dict={}
       profiles=[]
       profile_ids=[]
       for x in range(len(args[2])):
         for y in range(len(request.POST.getlist(args[1][0]))):
             list1 = list1 + gb[args[3][x]](gb[args[2][x]].objects.filter(level=request.POST.getlist(args[1][0])[y],project=request.POST.getlist(args[1][1])[y]),many=True).data 
        
       for x1 in range(len(list1)):
           
           if list1[x1]['profile'] not in profile_ids:
            profiles =profiles + ProfileSerializer(Profile.objects.filter(id=list1[x1]["profile"]),many=True).data
            profile_ids.append(list1[x1][args[1]])
       for x1 in range(len(profiles)):
           
           profiles_dict[profiles[x1]['id']] =  profiles[x1]
       #sorted(problem_list, key=attrgetter("date"))
       list1 = sorted(list1, key=itemgetter(args[1]))
       return Response({"list1":list1,"profiles":profiles_dict})
    else:
        return  Response( {"error":'this request method is not supported'})
@api_view(['GET'])
def ProjectCommentList(request):
      
       project_comment_list =[]
       for x in range(len(ML)):
          project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.all(),many=True).data 
      
       #sorted(problem_list, key=attrgetter("date"))
       
       all_project_comments = sorted(project_comment_list, key=itemgetter("date"))
       return Response(all_project_comments)   
@api_view(['GET','POST'])
def ProjectCommentList1(request):
      
       project_comment_list =[]
       for x in range(len(ML)):
          project_comment_list = project_comment_list + gb[SL[x]](gb[ML[x]].objects.all(),many=True).data 
      
       #sorted(problem_list, key=attrgetter("date"))
       
       all_project_comments = sorted(project_comment_list, key=itemgetter("date"))
       return Response(all_project_comments)        
class ProjectCommentViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProjectComment.objects.all()
    serializer_class = ProjectCommentSerializer
    permission_classes= pcv1
class CountryProjectCommentViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CountryProjectComment.objects.all()
    serializer_class = CountryProjectCommentSerializer
    permission_classes= pcv1     
class RegionProjectCommentViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegionProjectComment.objects.all()
    serializer_class = RegionProjectCommentSerializer
    permission_classes= pcv1 
    
class ZoneProjectCommentViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ZoneProjectComment.objects.all()
    serializer_class = ZoneProjectCommentSerializer
    permission_classes= pcv2
    
class WeredaProjectCommentViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WeredaProjectComment.objects.all()
    serializer_class = WeredaProjectCommentSerializer
    permission_classes= pcv1 
    
class CityProjectCommentViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CityProjectComment.objects.all()
    serializer_class = CityProjectCommentSerializer
    permission_classes= pcv1 
    
    
class KebeleProjectCommentViewSet(ViewSetCommonForAll):

    queryset = KebeleProjectComment.objects.all()
    serializer_class = KebeleProjectCommentSerializer
    permission_classes= pcv1                
class UserRegionProjectComment(ViewSetCommonForAll):
    queryset = RegionProjectComment.objects.all()
    serializer_class = RegionProjectCommentSerializer 
    def get_queryset(self):
            return RegionProjectComment.objects.filter(region=self.request.user.profile.region)
class UserZoneProjectComment(ViewSetCommonForAll):
    queryset = ZoneProjectComment.objects.all()    
    serializer_class = ZoneProjectCommentSerializer 
    def get_queryset(self):
            return ZoneProjectComment.objects.filter(region=self.request.user.profile.region)   
        
        
class UserWeredaProjectComment(ViewSetCommonForAll):
    queryset = WeredaProjectComment.objects.all()
    serializer_class = WeredaProjectCommentSerializer 
    def get_queryset(self):
            return WeredaProjectComment.objects.filter(region=self.request.user.profile.region)

class UserCityProjectComment(ViewSetCommonForAll):
    queryset = CityProjectComment.objects.all()
    serializer_class = CityProjectCommentSerializer 
    def get_queryset(self):
            return CityProjectComment.objects.filter(region=self.request.user.profile.region)
        
class UserKebeleProjectComment(ViewSetCommonForAll):
    queryset = KebeleProjectComment.objects.all()
    serializer_class = KebeleProjectCommentSerializer 
    def get_queryset(self):
            return KebeleProjectComment.objects.filter(region=self.request.user.profile.region) 
        
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