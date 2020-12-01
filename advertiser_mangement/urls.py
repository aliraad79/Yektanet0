from django.urls import path
from .views import show_ads, count_ad_click ,create_ad
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', show_ads, name='show-ad-all'),
    path('click/<int:ad_id>/', count_ad_click, name='count-ad-click'),
    path('ad/create/', create_ad , name='create-ad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)