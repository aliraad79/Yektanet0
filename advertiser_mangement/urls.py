from django.urls import path
from .views import show_ads, count_ad_click, CreateAd, CreateAdvertiser
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('ad/all', show_ads, name='show-all-ads'),
                  path('ad/click/<int:ad_id>/', count_ad_click, name='click-add'),
                  path('ad/create/', CreateAd.as_view(), name='create-ad'),
                  path('advertiser/create/', CreateAdvertiser.as_view(), name='create-advertiser'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
