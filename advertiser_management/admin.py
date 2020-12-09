from django.contrib import admin
from .models import Ad, Advertiser


def approve_ad(modeladmin, request, queryset):
    queryset.update(approve='True')


def disapprove_ad(modeladmin, request, queryset):
    queryset.update(approve='False')


approve_ad.short_description = "Mark selected Ad approved"
disapprove_ad.short_description = "Mark selected Ad disapproved"


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'advertiser', 'approve')
    list_filter = ('approve',)
    search_fields = ('title',)
    actions = [approve_ad, disapprove_ad]


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
