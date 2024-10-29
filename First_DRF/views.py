from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET' , 'POST'])
@permission_classes([AllowAny])
def item(request):
 try:
   uname=request.data['username']
   fname=request.data['firstname']
   email=request.data['email']
   lname=request.data['lastname']
   password=request.data['password']
   data1={
    'fname':fname,
    'lname':lname,
    'email':email,
    'uname':uname,
    'pass':password
   }
   user_data=User.objects.create_user(username=uname ,email=email , password=password)
   user_data.first_name=fname
   user_data.last_name=lname
   user_data.save()
   
   return Response("User Added Sucessfully")
 except:
  data1="Error creating the user please try again later"
 return Response(data1) 

class Data(APIView):
  
  def post(self,request):
    data=request.data['description']
    note=Notes.objects.create(description=data)
    note.save()
    return Response("Notes added seccess fully!")
  def get(self,request):
    data=Notes.objects.all()
    Serializer=NotesSerializer(data, many=True)
    return Response({
      'return data': Serializer.data
    })
  def put(self,request):
    data=Notes.objects.get(id=request.data['id'])
    data.description=request.data['description']
    data.save()
    return Response('data updated success fully')
  def delete(self , request):
    data=Notes.objects.get(id=request.data['id'])
    data.delete()
    return Response('Data deleted success fully')
  
class todolist(APIView):
  def post(self,request):
    title=request.data['title']
    description=request.data['description']
    status= True if request.data['status'] == 'true' else False
    
    data=ToDOList.objects.create(title=title,description=description,status=status)
    data.save()
    
    return JsonResponse('Task added to the to do list success fully')
  
  def get(self,request):
    data=ToDOList.objects.all()
    paginator=PageNumberPagination()
    paginationdata=paginator.paginate_queryset(data,request)
    
    Serializer=ToDoListSerializer(paginationdata, many =True)
    
    return paginator.get_paginated_response(Serializer.data)
    
  def patch(self,request):
    object=ToDOList.objects.get(id=request.data['id'])
    object.title=request.data['title']
    object.description=request.data['description']
    object.status=request.data['status']
    object.save()
    return JsonResponse({
      'Response':'Data has been updated success fully',
      'id':object.id,
      'title':object.title,
      'description':object.description,
      'status':object.status,
    })
  
  def delete(self,request):
    data=ToDOList.objects.get(id=request.data['id'])
    data.delete()
    
    return Response("task has been deleted seccess fully")
    