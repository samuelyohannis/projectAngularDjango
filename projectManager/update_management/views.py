from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Update(APIView):
   
    def get_object(self, pk1):
        try:
            return self.Model.objects.get(pk=pk1)
        except self.Model.DoesNotExist:
            raise Http404    
    @classmethod
    def as_view(cls, Serializer,Model,**kwargs):
        cls.Serializer  = Serializer
        cls.Model  = Model
        return super(Update,cls).as_view(**kwargs)
      
       
   
    
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = self.Serializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateFactory():
       
     return  type('',   (Update,), dict())    