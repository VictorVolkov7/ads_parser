from django.urls import path

from ads.api_views import AdRetrieveAPIView
from ads.apps import AdsConfig

app_name = AdsConfig.name

urlpatterns = [
    # ad routes
    path('ad/<int:ad_id>/', AdRetrieveAPIView.as_view(), name='ad-retrieve'),
]
