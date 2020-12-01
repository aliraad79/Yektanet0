from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertiser, Ad

# Create your views here.


def show_ads(request):
    advertisers = Advertiser.objects.all()
    context = {'advertisers':advertisers}
    return render(request,'advertiser_mangement/ads.html',context=context)


def count_ad_click(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    ad.add_click()
    ad.save()
    return redirect(ad.link)


def create_ad(request):
    return HttpResponse(request)
