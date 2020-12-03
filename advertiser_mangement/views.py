from django.shortcuts import render, redirect, get_list_or_404
from .models import Advertiser, Ad
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def show_ads(request):
    advertisers = get_list_or_404(Advertiser)
    context = {'advertisers': advertisers}
    return render(request, 'advertiser_mangement/ads.html', context=context)


def count_ad_click(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    ad.add_click()
    ad.add_view()
    return redirect(ad.link)


class CreateAd(CreateView):
    model = Ad
    fields = ['advertiser', 'title', 'image', 'link']


class CreateAdvertiser(CreateView):
    model = Advertiser
    fields = ['name']
