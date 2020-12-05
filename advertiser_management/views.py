from django.shortcuts import get_object_or_404
from .models import Advertiser, Ad
from django.views.generic import CreateView, RedirectView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin


class AdvertiserListView(ListView):
    model = Advertiser
    template_name = 'advertiser_management/ads.html'
    context_object_name = 'advertisers'

    def get(self, request, *args, **kwargs):
        ip = request.META.get('REMOTE_ADDR')
        for i in Advertiser.objects.all():
            for j in i.ads.all():
                j.add_view(ip)
        return super().get(request, *args, **kwargs)


class CountAdClick(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        ad.add_click(self.request.META.get('REMOTE_ADDR'))
        return ad.link


class CreateAd(SuccessMessageMixin, CreateView):
    model = Ad
    fields = ['advertiser', 'title', 'image', 'link']
    success_message = "Ad created successfully!!!"


class CreateAdvertiser(SuccessMessageMixin, CreateView):
    model = Advertiser
    fields = ['name']
    success_message = "Advertiser created successfully!!"


class AdvertiserDetail(DetailView):
    model = Advertiser
