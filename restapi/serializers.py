from rest_framework import serializers
from advertiser_management.models import Ad, Advertiser


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['id', 'name']