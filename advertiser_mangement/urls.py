from django.urls import path
from .views import CreateAd, CreateAdvertiser, CountAdClick, AdvertiserListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('ad/all', AdvertiserListView.as_view(), name='show-all-ads'),
                  path('ad/click/<int:ad_id>/', CountAdClick.as_view(), name='click-add'),
                  path('ad/create/', CreateAd.as_view(), name='create-ad'),
                  path('advertiser/create/', CreateAdvertiser.as_view(), name='create-advertiser'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
