from .models import Ad, Advertiser, View, Click


class IpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        # for ad_detail.html
        click_and_viewed_dic = {}
        for i in Ad.objects.all():
            click_and_viewed_hour = {}
            all_clicks = 0
            all_views = 0
            for z in range(0, 24):
                clicks = Click.objects.filter(ad_id=i.id, click_time__hour=z).count()
                views = View.objects.filter(ad_id=i.id, view_time__hour=z).count()
                all_clicks += clicks
                all_views += views
                if views != 0:
                    click_and_viewed_hour[str(z)] = (clicks, views, float("{0:.4f}".format(clicks / views)))
                else:
                    click_and_viewed_hour[str(z)] = (clicks, views, 0)
            click_and_viewed_dic[i] = (
                click_and_viewed_hour, all_clicks, all_views, float("{0:.4f}".format(all_clicks / all_views)))

            # a dictionary which it keys are ad objects and  it values are
            # 0 : a dic : keys = hour , value = (click in that hour, view in that hour, click per view in that hour)
            # 1 : count of all clicks of that ad
            # 2 : count of all views of that ad
            # 3 : click per view of that ad
            response.context_data['click_and_viewed_dic'] = click_and_viewed_dic

        return response
