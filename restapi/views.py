from django.shortcuts import render
from rest_framework import mixins, generics
from advertiser_management.models import Advertiser
from .serializers import AdvertiserSerializer
from rest_framework import viewsets


class AdvertiserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer


class AdvertiserDetail(generics.RetrieveAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
