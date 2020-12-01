from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertiser, Ad
from .forms import CreateAdForm

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
    if request.method == "POST":
        form = CreateAdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CreateAdForm()
    return render(request,'advertiser_mangement/create_ad.html',{'form':form})
