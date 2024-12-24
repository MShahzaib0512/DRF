from django.shortcuts import render
from .serializer import ItemSerializer
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class ModelViewsetPermissions(viewsets.ModelViewSet):
   queryset=User.objects.all()
   serializer_class=ItemSerializer
   permission_classes=[IsAuthenticated]
   authentication_classes=[SessionAuthentication]
   