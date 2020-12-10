from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advertiser_management.urls')),
    path('api/',include('restapi.urls')),
]
