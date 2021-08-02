from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class List(APIView):
   
    def get_object(self, pk):
        try:
            return self.Model.objects.get(pk=pk)
        except self.Model.DoesNotExist:
            raise Http404    
    @classmethod
    def as_view(cls, Serializer,Model,**kwargs):
        cls.Serializer  = Serializer
        cls.Model  = Model
        return super(List,cls).as_view(**kwargs)
      
       
   
    
    def get(self, request, format=None):
        object = self.Model.objects.all()
        serializer = self.Serializer(object, many=True)
        print(self.Serializer)
        return Response(serializer.data)
       
        
def listFactory():
       
     return  type('',   (List,), dict())    
       

# Create your views here.
