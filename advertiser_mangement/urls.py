from django.urls import path
from .views import show_ads, count_ad_click ,create_ad


app_name = 'advertiser_mangement'
urlpatterns = [
    path('ad/', show_ads, name='show-ad'),
    path('click/<int:ad_id>/', count_ad_click, name='count-ad-view'),
    path('ad/create/', create_ad , name='create-ad'),
]
