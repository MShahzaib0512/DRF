from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from rest_framework import status

#reset password imports
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.conf import settings 
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token


"""Some Basic Tasks Using DRF"""
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

class Item(APIView):
  def post(self, request):
    user_object=ItemSerializer(data=request.data)
    
    if not user_object.is_valid():
      return Response({ 'error': user_object.errors , 'message':'error craeating user !'})
    user_object.save()
    
    """TO CREATE SESSION WEB TOKENS WE USE MESTHOD BELOW"""
    
    # user = user_object.save()
    # myuser=User.objects.get(id=user.id)
    # user_token , _ =Token.objects.get_or_create(user=user)
    
    
    return Response({
      "status": 200,
      "message":"user craeted sucessfully",
      'payload':user_object.data,
      # "user_session_token":str(user_token)
    })

class Data(APIView):
  
  def post(self,request):
    data=request.data['description']
    note=Notes.objects.create(description=data)
    note.save()
    return Response("Notes added seccess fully!")
  def get(self,request):
    data=Notes.objects.all()
    print(data)
    Serializer=NotesSerializer(data, many=True)
    print(type(Serializer.data))
    return Response({
      'return data':Serializer.data
    })
  def put(self,request):
    object=Notes.objects.get(id=request.data['id'])
    object_data=NotesSerializer(object, data=request.data)
    if not object_data.is_valid():
      return Response({'status':403, "message":"An occured during data updating","error":object_data.errors})
    object_data.save()
    return Response({
      "status":200,
      "message":"data updated successfully",
      "payload" : object_data.data      
    })
  def delete(self , request):
    data=Notes.objects.get(id=request.data['id'])
    data.delete()
    return Response('Data deleted success fully')
  
class todolist(APIView):
  def post(self,request):
    
    if request.data.get('action') == 'create':
      return self.create_task(request)
    elif request.data.get('filter') == 'filter':
      return self.filter_task(request)
    else:
      return Response("invalid action please enter the correct action create for creaing and filter for filtering")
    
  def create_task(self,request):
    title=request.data['title']
    description=request.data['description']
    status= True if request.data['status'] == 'true' else False
    
    data=ToDOList.objects.create(title=title,description=description,status=status)
    data.save()
    
    return JsonResponse('Task added to the to do list success fully')
  
  def filter_task(self,request):
    status=request.data['status']
    print(status)
    if status == 'success':
      data=ToDOList.objects.filter(status=True)
      print(data)
      Serializer=ToDoListSerializer(data, many=True)
      return Response({
        'filtered data':Serializer.data
      })       
    else:
      data=ToDOList.objects.filter(status=False)
      print(data)
      Serializer=ToDoListSerializer(data, many=True)
      return Response({
        'filtered data':Serializer.data
      })
  
  def get(self,request):
    data=ToDOList.objects.all()
    paginator=PageNumberPagination()
    paginationdata=paginator.paginate_queryset(data,request)
    
    Serializer=ToDoListSerializer(paginationdata, many =True)
    
    return paginator.get_paginated_response(Serializer.data)
    
  def patch(self,request):
    object=ToDOList.objects.get(id=request.data['id'])
    
    object_data= ToDoListSerializer(object, data = request.data , partial =True)
    if not object_data.is_valid():
      return Response({'status':"403", "message":"An error occured while updating !", "error" : object_data.errors})
    object_data.save()
    
    return JsonResponse({
      'status':200,
      'Response':'Data has been updated success fully',
      'payload':object_data.data
    })
  
  def delete(self,request):
    data=ToDOList.objects.get(id=request.data['id'])
    data.delete()
    
    return Response("task has been deleted seccess fully")

class ContactManager(APIView):
  def post(self , request):
    
    if request.data.get("action")=='Create':
      return self.create_contact(request)
    elif request.data.get('action')=='filter':
      return self.filter_contact(request)
    else:
      return Response("invalid action defined")
    
  def create_contact(self,request):
    
    name1=request.data['name']
    phone=request.data['phone']
    email=request.data['email']
    
    data=ContactManagement.objects.create(name=name1,phone=phone,email=email)
    data.save()
    
    return Response("Contect added success fully!")
  
  def filter_contact(self,request):
    data=ContactManagement.objects.filter(name=request.data['name'])
    Serilaizer=ContactManagementSerializer(data,many=True)
    return Response({
      "Filtered data":Serilaizer.data
    })
    
  def get(self,request):
    data=ContactManagement.objects.all()
    paginator=PageNumberPagination()
    paginated_data=paginator.paginate_queryset(data,request)
    Serializer=ContactManagementSerializer(paginated_data,many=True)
        
    return paginator.get_paginated_response(Serializer.data)
    
  def put(self,request):
    object=ContactManagement.objects.get(id=request.data['id'])
    ser_data=ContactManagementSerializer(object ,data=request.data ,partial=True )
    if not ser_data.is_valid():
      return Response({'message':"An error occured!", "error":ser_data.errors})
    ser_data.save()
    payload=ser_data.data 
    
    return JsonResponse({
      "Data has been updated successfully":"Congrats",
      "payload":payload
    })
    
  def delete(self,request):
    data=ContactManagement.objects.get(id=request.data['id'])
    data.delete()
    
    return Response("Contact deleted sccessfully")
@permission_classes([AllowAny])  
class frogetpassword(APIView):
  
    def post(self,request):
      Serializer=PasswordResetRequestSerializer(data=request.data)
      try:
        if Serializer.is_valid():
            email = Serializer.validated_data['email']
            print(email)
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator().make_token(user)
            
            reset_url = request.build_absolute_uri(
                reverse('password-reset-confirm', kwargs={'token': token, 'uid': user.id})
            )
            
            subject = "Password reset link requested"
            message = (f"Click on the link below if you requested a password reset. "
                      f"Otherwise, you can ignore this email: {reset_url}")
            from_mail = settings.EMAIL_HOST_USER
            to_mail = [user.email]
            
            send_mail(subject, message, from_mail, to_mail, fail_silently=False)
            return Response("Password reset link was successfully sent to your email address. Check your email to reset your password.")
      except Exception as e:
          print(f"Error sending email: {e}")  # Debugging output
          return Response("Invalid email address provided or error in sending email.")       
@permission_classes([AllowAny])
class PasswordResetConfirm(APIView):
  
    def post(self, request, token, uid):
        user = get_object_or_404(User, id=uid)
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response(
                {"error": "Token has expired or is invalid. Please request a new one."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(
                {"message": "Password has been updated successfully"},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
