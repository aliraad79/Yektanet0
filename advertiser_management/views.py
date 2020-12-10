from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Advertiser, Ad, Click, View
from django.views.generic import RedirectView, ListView
from datetime import timedelta
from .serializers import AdvertiserSerializer, ShowAdSerializer, CreateAdSerializer
from rest_framework import viewsets


def ads_detail():
    """
        function to process data and show more data about ads
    """
    # estimate time for an ad
    time_to_watch_ad = {}
    estimated_time_to_click_ad = {}
    for click_object in Click.objects.all():
        view_object = View.objects.filter(view_time__lte=click_object.click_time, ip=click_object.ip,
                                          ad=click_object.ad).order_by('view_time').last()
        if click_object.ad in time_to_watch_ad.keys():
            time_to_watch_ad[click_object.ad] += click_object.click_time - view_object.view_time
        else:
            time_to_watch_ad[click_object.ad] = click_object.click_time - view_object.view_time

    for i, j in time_to_watch_ad.items():
        estimated_time_to_click_ad[i] = j / Click.objects.filter(ad=i).count()
    # set clicks and views
    click_and_viewed_dic = {}
    for i in Ad.objects.all():
        click_and_viewed_hour = {}
        all_clicks = 0
        all_views = 0
        for z in range(0, 24):
            clicks = Click.objects.filter(ad=i, click_time__hour=z).count()
            views = View.objects.filter(ad=i, view_time__hour=z).count()
            all_clicks += clicks
            all_views += views
            if views != 0:
                click_and_viewed_hour[str(z)] = (clicks, views, float("{0:.4f}".format(clicks / views)))
            else:
                click_and_viewed_hour[str(z)] = (clicks, views, 0)
        click_and_viewed_hour = {k: v for k, v in
                                 sorted(click_and_viewed_hour.items(), key=lambda item: item[1][2], reverse=True)}
        # check if ad has been clicked
        if i in estimated_time_to_click_ad.keys():
            # check if ad been viewed
            if all_views != 0:
                click_and_viewed_dic[i] = (
                    click_and_viewed_hour, all_clicks, all_views, float("{0:.4f}".format(all_clicks / all_views)),
                    estimated_time_to_click_ad[i])
            # check if ad not been viewed
            else:
                click_and_viewed_dic[i] = (
                    click_and_viewed_hour, all_clicks, all_views, 0, estimated_time_to_click_ad[i])
        # check if ad not been clicked
        else:
            # check if ad been viewed
            if all_views != 0:
                click_and_viewed_dic[i] = (
                    click_and_viewed_hour, all_clicks, all_views, float("{0:.4f}".format(all_clicks / all_views)),
                    timedelta(0))
            # check if ad not been viewed
            else:
                click_and_viewed_dic[i] = (
                    click_and_viewed_hour, all_clicks, all_views, 0, timedelta(0))
    # a dictionary which it keys are ad objects and  it values are
    # 0 : a dic : keys = hour , value = (click in that hour, view in that hour, click per view in that hour)
    # 1 : count of all clicks of that ad
    # 2 : count of all views of that ad
    # 3 : click per view of that ad
    # 4 : estimated time for an ad to be clicked
    return click_and_viewed_dic


class AdListView(ListView):
    model = Ad
    template_name = 'advertiser_management/ad_detail.html'
    context_object_name = 'ads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['click_and_viewed_dic'] = ads_detail()
        return context


class AdvertiserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing and creating advertiser.
    """
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    def list(self, request, *args, **kwargs):
        ip = request.META.get('REMOTE_ADDR')
        for i in Advertiser.objects.all():
            for j in i.ads.filter(approve=True):
                j.add_view(ip)
        return super().list(request, *args, **kwargs)


class AdViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing and creating ads.
    """
    queryset = Ad.objects.all()
    serializers = {
        'create': CreateAdSerializer,
        'default': ShowAdSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    @action(detail=False, methods=['GET'], name='Click add')
    def click(self, request, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        ad.add_click(self.request.META.get('REMOTE_ADDR'))
        return Response(ad.link)
