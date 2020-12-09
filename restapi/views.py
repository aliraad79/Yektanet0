from django.shortcuts import render
from rest_framework import mixins, generics
from advertiser_management.models import Advertiser
from .serializers import AdvertiserSerializer


class AdvertiserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
