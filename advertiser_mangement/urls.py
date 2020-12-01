from django.urls import path
from .views import show_ads, count_ad_click ,create_ad
from django.conf.urls.static import static
from django.conf import settings

app_name = 'advertiser_mangement'
urlpatterns = [
    path('ad/', show_ads, name='show-ad'),
    path('click/<int:ad_id>/', count_ad_click, name='count-ad-view'),
    path('ad/create/', create_ad , name='create-ad'),
] + static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)