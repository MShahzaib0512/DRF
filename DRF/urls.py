from django.contrib import admin
from django.urls import path, include

# Include router.urls in urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('First_DRF.urls')),
    path('',include('geekyshow.urls')),
    path('auth/',include('rest_framework.urls')),
    path("permissions/",include("permissions.urls")),
]

