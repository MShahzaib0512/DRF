from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', ModelViewsetPermissions, basename='user')

urlpatterns = [
  path('', include(router.urls)),
]