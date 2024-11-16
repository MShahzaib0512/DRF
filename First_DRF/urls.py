from django.urls import path ,include
from .views import *

urlpatterns = [
    path('item', item),
    path('data', Data.as_view()),
    path('todolist', todolist.as_view()),
    path('ContactManager', ContactManager.as_view()),
    path('Item', Item.as_view()),
    
    path('password-reset-link',frogetpassword.as_view()),
    path('password-reset-confirm/<str:token>/<int:uid>/', PasswordResetConfirm.as_view()),
]