from django.urls import path
from .views import CreateAd, CreateAdvertiser, CountAdClick, AdvertiserListView, AdvertiserDetail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('ad/all', AdvertiserListView.as_view(), name='show-all-ads'),
                  path('ad/click/<int:ad_id>/', CountAdClick.as_view(), name='click-add'),
                  path('ad/create/', CreateAd.as_view(), name='create-ad'),
                  path('advertiser/create/', CreateAdvertiser.as_view(), name='create-advertiser'),
                  path('advertiser/detail/<int:pk>', AdvertiserDetail.as_view(), name='detail-advertiser'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
