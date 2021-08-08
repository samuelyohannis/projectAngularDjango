
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
    
    
 
class Mutiple(Create):
  @classmethod
  def as_view(self, Serializer,Model,**kwargs):
        self.Serializer  = Serializer
        self.Model  = Model
        
        return super(Mutiple,self).as_view(**kwargs)
  def get_object(self, pk):
        try:
            return self.Model.objects.get(pk=pk)
        except self.Model.DoesNotExist:
            raise Http404  
  def post(self, request, *args, **kwargs):
   
    serializer = self.Serializer(data=request.data)
    
    
            
    ''' if serializer.is_valid(raise_exception=True):
              files = request.FILES.getlist('files')
              object = self.get_object(request.POST['related_key_value'])
              for f in files:
                related_object = self.Model(file=f)  
                object[request.POST['related_key']].add(related_object)
                serializer = self.Serializer(data={request.data})
                serializer.save()
                self.Model.objects.create(f)
    return Response({
     self.Model.objects.create(file)
    })    '''
    
 