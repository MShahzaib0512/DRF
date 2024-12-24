from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view 
from .models import Student
# Create your views here.
@api_view(['GET' , 'POST'])
def student_create(request):
 if request.method == 'POST':
  print(request.data)
  serializer = studentSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response(
    {
     'data':serializer.data,
     'message':"user created",
     })
  return JsonResponse(serializer.errors,safe=False)
 elif request.method == 'GET':
  
  object=Student.objects.get(id=request.data['id'])
  print(object)
  
  serializer= studentSerializer(object)
  print(serializer.data)
  return Response({
   'data':serializer.data
   })  
 return JsonResponse ("error creating student",safe=False)
@api_view(['POST'])
def create_user(request):
   serializer = UserSerializer(data = request.data)
   if serializer.is_valid():
      serializer.save()
      return JsonResponse('User created successfully' , safe= False)
   else:
      error = serializer.errors 
      return JsonResponse(error)
   
""" GnericAPIView practice""" 

from rest_framework.mixins import ListModelMixin , CreateModelMixin , UpdateModelMixin , DestroyModelMixin , RetrieveModelMixin
from rest_framework.generics import GenericAPIView

# without id

class GenericItem(ListModelMixin , CreateModelMixin, GenericAPIView):
   queryset = User.objects.all()
   serializer_class = ItemSerializer
   
   def get(self , request , *args, **kwargs):
      return self.list(request , *args, **kwargs)
   
   def post(self , request , *args, **kwargs):
      return self.create(request , *args, **kwargs)
   
# with id
class GenericItemById(GenericAPIView , UpdateModelMixin , DestroyModelMixin , RetrieveModelMixin ):
   
   queryset = User.objects.all()
   serializer_class = ItemSerializer
   
   def get(self , request , *args, **kwargs):
      return self.retrieve(request , *args, **kwargs)
   
   def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)
   
   def patch(self, request, *args, **kwargs):
     return self.partial_update(request, *args, **kwargs)
  
   def delete(self, request, *args, **kwargs):
     return self.destroy(request, *args, **kwargs)
     
"""now using concreate API View"""

from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView

class ConcreteItem(ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = ItemSerializer
   
class ConcreteItemById(RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = ItemSerializer
   
""" when using only viewset we have to only one class for both urls with or without id by adding the router in the mian url that maanges the routhing of our class or view set no we start 

Model view set it also have an other version ReadOnlyModelViewset which is used to only read data it performs only two tasks get and restrive get return the list of all the records in the model and retrive send the details of specific model attribute by id

"""

from rest_framework import viewsets

class ModelViewsetItem(viewsets.ModelViewSet):
   queryset=User.objects.all()
   serializer_class=ItemSerializer
   
   """
      BASIC AUTHENTICATION USING  DRF:-
            the method is used for individually authenticate each wvie if you want to authenticate all the views or most of the views with the same authentication you can use the global authenticaion in the settings AS 
   
            REST_FRAMEWORK={
               'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentications.BasicAuthentication'],
               'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated'],
            }
            
            and this global authentication can be changed by overriding the class at the view itself as we individually define the authentication and the permission at the view   
   
   """
# from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# class ModelViewsetPermissions(viewsets.ModelViewSet):
#    queryset=User.objects.all()
#    serializer_class=ItemSerializer
#    permission_classes=[IsAuthenticated]
#    authentication_classes=[BasicAuthentication]
   
   """
      SESSION AUTHENTICATION:-
      
      in session authentication we need to use the django restframework builtin urls beacuse it not ask for username and password in the prompt as in the basics authentication other wise it shows the error: authentication credential not provided for being safe from this error we used ubilt in urls as 
      
      path('auth/,include('rest_framework) , name='rest_framework')
      
      now the should ask for he login/logout  from the user for authentication credentials
   
   """
   
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class ModelViewsetPermissions(viewsets.ModelViewSet):
   queryset=User.objects.all()
   serializer_class=ItemSerializer
   permission_classes=[IsAuthenticated]
   authentication_classes=[SessionAuthentication]
   