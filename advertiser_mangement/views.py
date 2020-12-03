from django.shortcuts import render, redirect, get_list_or_404
from .models import Advertiser, Ad
from .forms import CreateAdForm, CreateAdvertiserForm
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


def create_advertiser(request):
    if request.method == "POST":
        form = CreateAdvertiserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-all-ads')
    else:
        form = CreateAdvertiserForm()
    return render(request, 'advertiser_mangement/create_advertiser.html', {'form': form})
