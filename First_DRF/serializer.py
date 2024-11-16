from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

""" Notes API with crud operations  """
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password','first_name','last_name' ]
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if not user.id:
          raise serializers.ValidationError("User ID not created")
        return user

class NotesSerializer(serializers.ModelSerializer):
 
 class Meta:
  model=Notes
  fields=['id','description']
  
class ToDoListSerializer(serializers.ModelSerializer):
 class Meta:
  model=ToDOList
  fields='__all__'
  
class ContactManagementSerializer(serializers.ModelSerializer):
  class Meta:
    phone=serializers.CharField(source='phone',read_only=True)
    model=ContactManagement
    fields='__all__'
    
class PasswordResetRequestSerializer(serializers.Serializer):
  email=serializers.EmailField()
  
  def validate_email(self, value):
    if not User.objects.filter(email=value).exists():
      raise serializers.ValidationError("User with the eamil not found")
    return value
  
class PasswordResetConfirmSerializer(serializers.Serializer):
  
  new_password=serializers.CharField(write_only=True, min_length=8)
  
  def save(self,user):
    user.set_password(self.validated_data['new_password'])
    user.save()
    return user