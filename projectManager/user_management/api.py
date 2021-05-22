from rest_framework import viewsets,permissions,generics
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from .models import *
from django.shortcuts import get_object_or_404



pcv1 = [permissions.IsAuthenticated]
pcv2 = [permissions.AllowAny,]
prcv = [MultiPartParser,FormParser,JSONParser,]

# if (False):
#     from constants import *  
class ViewSetCommonForAll(viewsets.ModelViewSet):
    permission_classes = pcv2 
    parser_classes = prcv
    
class UserViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes= (permissions.AllowAny,)

class GroupViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows groups to be viewed or edited. """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes= (permissions.AllowAny,)  
class ProfileViewSet(ViewSetCommonForAll):
    """
    API endpoint that allows groups to be viewed or edited. """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes= (permissions.AllowAny,)  
''' class UserProfileViewSet(ViewSetCommonForAll):
    permission_classes= (permissions.AllowAny,)  
    serializer_class = ProfileSerializer 
     
     
    def get_object(self):
        return self.request.user.profile
    def get_queryset(self):
            return  Profile.objects.filter(region=self.request.user.profile)    '''      
        
        
class UserProfileViewSet(generics.RetrieveAPIView):
  permission_classes = [
    permissions.AllowAny,
  ]
  serializer_class = ProfileSerializer 

  def get_object(self):
    return self.request.user.profile        
class UserProfilesViewSet(generics.ListAPIView):
  permission_classes = [
    permissions.AllowAny,
  ]
  serializer_class = ProfileSerializer 

  def get_queryset(self):
    profiles = Profile.objects.all()
    return profiles