from django.urls import path, include
from .views import AdvertiserViewSet, AdViewSet, AdCreate, AdvertiserCreate
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'advertiser', AdvertiserViewSet)
router.register(r'ad', AdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/ad/', AdCreate.as_view(), name='create-ad'),
    path('create/advertiser/', AdvertiserCreate.as_view(), name='create-advertiser'),
]
