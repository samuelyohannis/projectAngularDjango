
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
    
    
 
class CreateWithRelatedFile(APIView):
  @classmethod
  def as_view(self,Serializer,RelatedSerializer,Model,RelatedModel,RelatedName,**kwargs):
        self.Serializer  = Serializer
        self.Model  = Model
        self.RelatedModel = RelatedModel
        self.relatedKeyName = RelatedName
        self.RelatedSerializer  = RelatedSerializer
        
        return super(CreateWithRelatedFile,self).as_view(**kwargs)
  def get_object(self, pk):
        try:
            return self.Model.objects.get(pk=pk)
        except self.Model.DoesNotExist:
            raise Http404  
  def post(self, request, *args, **kwargs):
       response = {}
       serializer = self.Serializer(data=request.data)
     
       if serializer.is_valid():
           response = serializer.save()
           print(response)
           for x in range(len((request.FILES.getlist(f"{self.relatedKeyName}s")))):
            object = self.Model.objects.get(pk=response.id)
            related_object = self.RelatedModel.objects.create(file=(request.FILES.getlist(f"{self.relatedKeyName}s")[x]));
            getattr(object,f"{self.relatedKeyName}_set").add(related_object)
       response = self.Model.objects.get(pk=response.id)
       return Response(self.Serializer(response).data  , status=status.HTTP_201_CREATED)   
    
    
class MultipleFileUpload(APIView):
  @classmethod
  def as_view(self,FileSerializer,FileModel,**kwargs):
        self.FileSerializer  = FileSerializer
        self.FileModel  = FileModel
        return super(MultipleFileUpload,self).as_view(**kwargs)
  def get_object(self, pk):
        try:
            return self.FileModel.objects.get(pk=pk)
        except self.FileModel.DoesNotExist:
            raise Http404  
  def post(self, request, *args, **kwargs):
       response = {}
       serializer = self.FileSerializer(data=request.data)
     
       if serializer.is_valid():
            for x in range(len((request.FILES.getlist("files")))):
               
             response= response + self.FileSerializer.create(file=(request.FILES.getlist("files")[x]))
        
       return Response(response  , status=status.HTTP_201_CREATED)   
    
    
  
  
def multipleFileUploadFactory():
       
     return  type('',   (MultipleFileUpload,), dict())  
  
def createWithRelatedFileFactory():
       
     return  type('',   (CreateWithRelatedFile,), dict())                

    
 