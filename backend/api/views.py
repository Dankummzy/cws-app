from rest_framework.views import APIView
from rest_framework.response import Response
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from django.core.cache import cache
from .services.currency_service import fetch_exchange_rates
from .services.weather_service import fetch_weather
from .services.stock_service import fetch_stock_data
from .serializers import ConversionSerializer, WeatherSerializer, StockSerializer

@method_decorator(ratelimit(key='ip', rate='5/m', block=True), name='dispatch')
class CurrencyConversionView(APIView):
    def get(self, request):
        serializer = ConversionSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            cache_key = f"currency_{data['base_currency']}_{data['target_currency']}_{data['amount']}"
            cached_result = cache.get(cache_key)
            if cached_result:
                return Response(cached_result)
            
            rates = fetch_exchange_rates()
            if 'error' in rates:
                return Response({'error': rates['error']}, status=400)
            
            if rates and 'rates' in rates:
                base_rate = rates['rates'].get(data['base_currency'])
                target_rate = rates['rates'].get(data['target_currency'])
                if base_rate and target_rate:
                    conversion_rate = target_rate / base_rate
                    result = {'converted_amount': data['amount'] * conversion_rate, 'rate': conversion_rate}
                    cache.set(cache_key, result, timeout=3600)
                    return Response(result)
                else:
                    return Response({'error': f"Currency rates for {data['base_currency']} or {data['target_currency']} not found in rates"}, status=400)
            else:
                return Response({'error': 'Failed to fetch exchange rates or invalid base currency'}, status=400)
        return Response(serializer.errors, status=400)

@method_decorator(ratelimit(key='ip', rate='5/m', block=True), name='dispatch')
class WeatherView(APIView):
    def get(self, request):
        serializer = WeatherSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            cache_key = f"weather_{data['city']}"
            cached_weather = cache.get(cache_key)
            if cached_weather:
                return Response(cached_weather)

            weather_data = fetch_weather(data['city'])
            if weather_data:
                cache.set(cache_key, weather_data, timeout=3600)
                return Response(weather_data)
            return Response({'error': 'Weather data not found'}, status=400)
        return Response(serializer.errors, status=400)

@method_decorator(ratelimit(key='ip', rate='5/m', block=True), name='dispatch')
class StockPriceView(APIView):
    def get(self, request):
        serializer = StockSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            cache_key = f"stock_{data['symbol']}"
            cached_stock = cache.get(cache_key)
            if cached_stock:
                return Response(cached_stock)

            stock_data = fetch_stock_data(data['symbol'])
            if stock_data and 'Time Series (1min)' in stock_data:
                latest_time = sorted(stock_data['Time Series (1min)'].keys())[-1]
                latest_data = stock_data['Time Series (1min)'][latest_time]
                result = {
                    'symbol': data['symbol'],
                    'latest_time': latest_time,
                    'prices': latest_data
                }
                cache.set(cache_key, result, timeout=3600)
                return Response(result)
            return Response({'error': 'Stock data not found'}, status=400)
        return Response(serializer.errors, status=400)