from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from django.contrib.auth import authenticate,login
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)
# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    data =request.data
    print(request.data)
    serializer = self.get_serializer(data=request.data)
    # user1=authenticate(request,username=data.username,password=data.password)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    
    return Response({
      "user": UserSerializer1(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })
  
     
# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
   
    serializer.is_valid(raise_exception=True)
          
  
    user1 = authenticate(request,username=request.data["username"],password=request.data["password"])
    user1=login(request,user1)  
    user = serializer.validated_data
    print(get_all_logged_in_users())
    print('it is me')
    _, token = AuthToken.objects.create(user)
    
    return Response({
      "user": UserSerializer1(user, context=self.get_serializer_context()).data,
      "token": token
    })

# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer1

  def get_object(self):
    return self.request.user
