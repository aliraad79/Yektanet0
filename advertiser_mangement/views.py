from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Advertiser, Ad
from django.views.generic import CreateView, RedirectView


def show_ads(request):
    advertisers = get_list_or_404(Advertiser)
    context = {'advertisers': advertisers}
    return render(request, 'advertiser_mangement/ads.html', context=context)


class CountAdClick(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        ad.add_click()
        ad.add_view()
        return ad.link


class CreateAd(CreateView):
    model = Ad
    fields = ['advertiser', 'title', 'image', 'link']


class CreateAdvertiser(CreateView):
    model = Advertiser
    fields = ['name']
