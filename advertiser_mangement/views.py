from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertiser, Ad

# Create your views here.


def show_ads(request):
    advertisers = Advertiser.objects.all()
    context = {'advertisers':advertisers}
    return render(request,'advertiser_mangement/ads.html',context=context)


def count_ad_view(request, ad_id):
    return HttpResponse(request)


def create_ad(request):
    return HttpResponse(request)
