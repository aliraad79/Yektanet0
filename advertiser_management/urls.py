from django.urls import path
from .views import AdListView, AdViewSet, AdvertiserViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ad', AdViewSet)
router.register(r'advertiser', AdvertiserViewSet)
ad_click = AdViewSet.as_view({'get': 'click'})

urlpatterns = [
                  path('ad/click/<int:ad_id>/', ad_click, name='click-add'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
