from django.contrib import admin
from .models import Ad, Advertiser


@admin.register(Ad)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('title', 'advertiser', 'approve')
    list_filter = ('approve',)
    search_fields = ('title',)


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
