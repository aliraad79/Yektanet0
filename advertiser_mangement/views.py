from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show_ads(request):
    return HttpResponse(request)


def count_ad_view(request, ad_id):
    return HttpResponse(request)


def create_ad(request):
    return HttpResponse(request)
