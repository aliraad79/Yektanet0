from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Advertiser, Ad
from .serializers import ShowAdSerializer, CreateAdSerializer, AdvertiserSerializer, DetailAdSerializer


class AdViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing and creating ads.
    """
    queryset = Ad.objects.all()
    serializers = {
        'create': CreateAdSerializer,
        'update': CreateAdSerializer,
        'list': DetailAdSerializer,
        'default': ShowAdSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    @action(detail=True, methods=['GET'], name='Click ad')
    def click(self, request, pk):
        ad = self.get_queryset().get(pk=pk)
        ad.add_click(request.META.get('REMOTE_ADDR'))
        return Response(ad.link)


class AdvertiserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing and creating advertiser.
    """
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    def list(self, request, *args, **kwargs):
        ip = request.META.get('REMOTE_ADDR')
        for i in Advertiser.objects.all():
            for j in i.ads.filter(approve=True):
                j.add_view(ip)
        return super().list(request, *args, **kwargs)
