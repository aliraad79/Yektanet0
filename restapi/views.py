from rest_framework import generics
from advertiser_management.models import Advertiser, Ad
from .serializers import AdvertiserSerializer, AdSerializer
from rest_framework import viewsets


class AdvertiserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer


class AdViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreate(generics.CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdvertiserCreate(generics.CreateAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
