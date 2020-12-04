from django.shortcuts import get_object_or_404
from .models import Advertiser, Ad
from django.views.generic import CreateView, RedirectView, ListView


class AdvertiserListView(ListView):
    model = Advertiser
    template_name = 'advertiser_management/ads.html'
    context_object_name = 'advertisers'


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
