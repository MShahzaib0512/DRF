from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

# Create a router instance
router = DefaultRouter()
router.register('users', ModelViewsetPermissions, basename='user')
urlpatterns = [
    path('student' , student_create , name='student'),
    path('create_user' , create_user , name='create_user'),
    
    # Generic api view urls
    
    path('Item' , GenericItem.as_view()),
    path('ItemById/<int:pk>' , GenericItemById.as_view()),
    
    # concrete api view urls
    
    path('Item' , ConcreteItem.as_view()),
    path('ItemById/<int:pk>' , ConcreteItemById.as_view()),
    
    # model viewset urls
    
    path('', include(router.urls)),
]