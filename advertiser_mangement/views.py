from django.shortcuts import render, redirect, get_list_or_404
from .models import Advertiser, Ad
from .forms import CreateAdForm, CreateAdvertiserForm


def show_ads(request):
    advertisers = get_list_or_404(Advertiser)
    context = {'advertisers': advertisers}
    return render(request, 'advertiser_mangement/ads.html', context=context)


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
            return redirect('show-all-ads')
    else:
        form = CreateAdForm()
    return render(request, 'advertiser_mangement/create_ad.html', {'form': form})


def create_advertiser(request):
    if request.method == "POST":
        form = CreateAdvertiserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-all-ads')
    else:
        form = CreateAdvertiserForm()
    return render(request, 'advertiser_mangement/create_advertiser.html', {'form': form})
