from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Detail(APIView):
   
    def get_object(self, pk1):
        try:
            return self.Model.objects.get(pk=pk1)
        except self.Model.DoesNotExist:
            raise Http404    
    @classmethod
    def as_view(cls, Serializer,Model,**kwargs):
        cls.Serializer  = Serializer
        cls.Model  = Model
        return super(Detail,cls).as_view(**kwargs)
      
       
   
    
    def get(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = self.Serializer(object)
       
        return Response(serializer.data)
       