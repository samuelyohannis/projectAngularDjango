
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


""" def Create1(request):
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 """


class Create(APIView):
    """  def __init__(self, Serializer, **kwargs):
        self.Serializer = Serializer
        super(Create,self).__init__(**kwargs) """
        
    @classmethod
    def as_view(cls, Serializer,Model,**kwargs):
        cls.Serializer  = Serializer
        cls.Model  = Model
        return super(Create,cls).as_view(**kwargs)
      
       
    def post(self, request, format=None,**kwargs):
        serializer = self.Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)