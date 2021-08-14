
from typing import overload
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Crud(APIView):
    
    @classmethod
    def as_view(self, Serializer,Model,**kwargs):
        self.Serializer  = Serializer
        self.Model  = Model
        
        return super(Crud,self).as_view(**kwargs)
    def get_object(self, pk):
        try:
            return self.Model.objects.get(pk=pk)
        except self.Model.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        object = self.Model.objects.all()
        serializer = self.Serializer(object, many=True)
       
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = self.Serializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def post(self, request, format=None):
        serializer = self.Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CrudWithRelatedFile(APIView):
    
    @classmethod
    def as_view(self,Serializer,RelatedSerializer,Model,RelatedModel,RelatedName,**kwargs):
        self.Serializer  = Serializer
        self.Model  = Model
        self.RelatedModel = RelatedModel
        self.relatedKeyName = RelatedName
        self.RelatedSerializer  = RelatedSerializer
        
        
        return super(CrudWithRelatedFile,self).as_view(**kwargs)
    def get_object(self, pk):
        try:
            return self.Model.objects.get(pk=pk)
        except self.Model.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        object = self.Model.objects.all()
        serializer = self.Serializer(object, many=True)
       
        return Response(serializer.data)
    def put(self, request, pk, format=None):
         response = {}
         object = self.get_object(pk)
         serializer = self.Serializer(object, data=request.data)
         if serializer.is_valid():
           response = serializer.save()
           print(response)
           for x in range(len((request.FILES.getlist("files")))):
            object = self.Model.objects.get(pk=response.id)
            related_object = self.RelatedModel.objects.create(file=(request.FILES.getlist("files")[x]));
            getattr(object,f"{self.relatedKeyName}_set").add(related_object)
           response = self.Model.objects.get(pk=response.id)
           return Response(self.Serializer(response).data  , status=status.HTTP_201_CREATED) 
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def post(self, request, format=None):
        response = {}
        serializer = self.Serializer(data=request.data)
     
        if serializer.is_valid():
           response = serializer.save()
           print(response)
           for x in range(len((request.FILES.getlist("files")))):
            object = self.Model.objects.get(pk=response.id)
            related_object = self.RelatedModel.objects.create(file=(request.FILES.getlist("files")[x]));
            getattr(object,f"{self.relatedKeyName}_set").add(related_object)
           response = self.Model.objects.get(pk=response.id)
           return Response(self.Serializer(response).data  , status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def crudWithRelatedFileFactory():
       
     return  type('',   (CrudWithRelatedFile,), dict())    
       
def crudFactory():
       
     return  type('',   (Crud,), dict())    
   