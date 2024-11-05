from django.urls import path ,include
from .views import *

urlpatterns = [
    path('item', item, name="item"),
    path('data', Data.as_view(), name="data"),
    path('todolist', todolist.as_view(), name="todolist"),
    path('ContactManager', ContactManager.as_view(), name="ContactManager"),
]