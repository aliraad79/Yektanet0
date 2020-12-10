from django.urls import path, include
from .views import AdvertiserViewSet, AdvertiserDetail
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'advertiser', AdvertiserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
