from rest_framework import serializers
from .models import Ad, Advertiser, Click, View
from datetime import timedelta


def ad_detail(ad):
    """
        function to process data and show more data about ads
    """
    # estimate time for an ad
    time_to_watch_ad = timedelta(0)
    all_clicks = Click.objects.filter(ad=ad).count()
    all_views = View.objects.filter(ad=ad).count()
    for click_object in Click.objects.filter(ad=ad):
        view_object = View.objects.filter(view_time__lte=click_object.click_time, ip=click_object.ip).order_by(
            'view_time').last()
        if view_object:
            time_to_watch_ad += click_object.click_time - view_object.view_time

    if all_clicks != 0:
        estimated_time_to_click_ad = time_to_watch_ad / all_clicks
    else:
        estimated_time_to_click_ad = 0
    # set clicks and views
    click_and_viewed_hour = {}
    for z in range(0, 24):
        clicks = Click.objects.filter(ad=ad, click_time__hour=z).count()
        views = View.objects.filter(ad=ad, view_time__hour=z).count()
        if views != 0:
            click_and_viewed_hour[str(z)] = (clicks, views, float("{0:.4f}".format(clicks / views)))
        else:
            click_and_viewed_hour[str(z)] = (clicks, views, 0)
    click_and_viewed_hour = {k: v for k, v in
                             sorted(click_and_viewed_hour.items(), key=lambda item: item[1][2], reverse=True)}
    # check if ad not been viewed
    if all_views != 0:
        click_and_viewed_dic = (
            click_and_viewed_hour, all_clicks, all_views, float("{0:.4f}".format(all_clicks / all_views)),
            estimated_time_to_click_ad)
    else:
        click_and_viewed_dic = (click_and_viewed_hour, all_clicks, all_views, 0, estimated_time_to_click_ad)

    # a dictionary
    # 0 : a dic : keys = hour , value = (click in that hour, view in that hour, click per view in that hour)
    # 1 : count of all clicks of ad
    # 2 : count of all views of  ad
    # 3 : click per view of  ad
    # 4 : estimated time for  ad to be clicked
    return click_and_viewed_dic


class CreateAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'image', 'link', 'advertiser']


class ShowAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'image', 'link', 'approve', 'advertiser']


class DetailAdSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField('ad_detail')

    def ad_detail(self, ad):
        return ad_detail(ad)

    class Meta:
        model = Ad
        fields = ['id', 'title', 'image', 'link', 'approve', 'advertiser', 'detail']


class AdvertiserSerializer(serializers.ModelSerializer):
    ads = ShowAdSerializer(many=True, read_only=True, source="approved_ads")

    class Meta:
        model = Advertiser
        fields = ['id', 'name', 'ads']
