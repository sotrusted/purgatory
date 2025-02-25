from django.urls import path
from .views import HomePageView, AboutPageView, ShopPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('shop/', ShopPageView.as_view(), name='shop'),
]
