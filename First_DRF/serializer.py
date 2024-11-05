from .models import *
from rest_framework import serializers

""" Notes API with crud operations  """
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