from rest_framework import serializers
from .models import Ad, Advertiser


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['id', 'name']


class CreateAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'image', 'link', 'advertiser']


class ShowAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'image', 'link', 'approve', 'advertiser']
