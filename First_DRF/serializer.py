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