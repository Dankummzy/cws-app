from django.urls import path
from .views import CurrencyConversionView, WeatherView, StockPriceView

urlpatterns = [
    path('convert/', CurrencyConversionView.as_view(), name='convert'),
    path('weather/', WeatherView.as_view(), name='weather'),
    path('stock/', StockPriceView.as_view(), name='stock'),
]
