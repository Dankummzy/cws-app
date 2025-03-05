# from django.test import TestCase
# from rest_framework.test import APIClient
# from unittest.mock import patch
# import os


# class APITestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.currency_url = '/api/convert/'
#         self.weather_url = '/api/weather/'
#         self.stock_url = '/api/stock/'

#     @patch('api.services.currency_service.fetch_exchange_rates')
#     def test_currency_conversion_success(self, mock_fetch_exchange_rates):
#         # Mock exchange rate data
#         mock_fetch_exchange_rates.return_value = {
#             'rates': {'USD': 1.0, 'EUR': 0.9587507094755252}
#         }

#         response = self.client.get(self.currency_url, {
#             'base_currency': 'USD',
#             'target_currency': 'EUR',
#             'amount': 100
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('converted_amount', response.data)
#         self.assertEqual(response.data['converted_amount'], 95.87507094755252)


#     @patch('api.services.currency_service.fetch_exchange_rates')
#     def test_currency_conversion_invalid_currency(self, mock_fetch_exchange_rates):
#         mock_fetch_exchange_rates.return_value = {
#             'rates': {'USD': 1.0}
#         }

#         response = self.client.get(self.currency_url, {
#             'base_currency': 'USD',
#             'target_currency': 'XYZ',
#             'amount': 100
#         })
#         self.assertEqual(response.status_code, 400)
#         self.assertIn('error', response.data)

#     @patch('api.services.weather_service.fetch_weather')
#     def test_weather_success(self, mock_fetch_weather):
#         # Mock weather data to match actual structure
#         mock_fetch_weather.return_value = {
#             'coord': {'lon': -0.1257, 'lat': 51.5085},
#             'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}],
#             'base': 'stations',
#             'main': {'temp': 7.21, 'feels_like': 2.85, 'temp_min': 6.68, 'temp_max': 7.86, 'pressure': 1012, 'humidity': 68},
#             'visibility': 10000,
#             'wind': {'speed': 8.75, 'deg': 280},
#             'clouds': {'all': 14},
#             'dt': 1734896868,
#             'sys': {'country': 'GB'},
#             'name': 'London'
#         }

#         response = self.client.get(self.weather_url, {'city': 'London'})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('main', response.data)
#         self.assertIn('temp', response.data['main'])
#         # Use delta for a small absolute tolerance
#         self.assertAlmostEqual(response.data['main']['temp'], 7.21, delta=0.1)


#     @patch('api.services.weather_service.fetch_weather')
#     def test_weather_invalid_city(self, mock_fetch_weather):
#         mock_fetch_weather.return_value = None

#         response = self.client.get(self.weather_url, {'city': 'InvalidCity'})
#         self.assertEqual(response.status_code, 400)
#         self.assertIn('error', response.data)

#     @patch('api.services.stock_service.fetch_stock_data')
#     def test_stock_price_success(self, mock_fetch_stock_data):
#         # Mock stock data
#         mock_fetch_stock_data.return_value = {
#             'Time Series (1min)': {
#                 '2023-12-21 15:30:00': {
#                     '1. open': '255.4750',
#                     '2. high': '260.0',
#                     '3. low': '250.0',
#                     '4. close': '258.0',
#                     '5. volume': '1200'
#                 }
#             }
#         }

#         response = self.client.get(self.stock_url, {'symbol': 'AAPL'})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('prices', response.data)
#         self.assertEqual(response.data['prices']['1. open'], '255.4750')

#     @patch('api.services.stock_service.fetch_stock_data')
#     def test_stock_price_invalid_symbol(self, mock_fetch_stock_data):
#         mock_fetch_stock_data.return_value = None

#         response = self.client.get(self.stock_url, {'symbol': 'INVALID'})
#         self.assertEqual(response.status_code, 400)
#         self.assertIn('error', response.data)

#     @patch('django.core.cache.cache.get')
#     @patch('django.core.cache.cache.set')
#     @patch('api.services.currency_service.fetch_exchange_rates')
#     def test_currency_conversion_cache(self, mock_fetch_exchange_rates, mock_cache_set, mock_cache_get):
#         # Mock cached data
#         mock_cache_get.return_value = {'converted_amount': 85.0, 'rate': 0.85}
        
#         response = self.client.get(self.currency_url, {
#             'base_currency': 'USD',
#             'target_currency': 'EUR',
#             'amount': 100
#         })
        
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['converted_amount'], 85.0)
#         mock_fetch_exchange_rates.assert_not_called()  # Ensure service isn't called due to cache


# class IntegrationTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.currency_url = '/api/convert/'
#         self.weather_url = '/api/weather/'
#         self.stock_url = '/api/stock/'
        
#         # Load real API keys from environment variables
#         self.currency_api_key = os.getenv('CURRENCY_API_KEY', 'YOUR_CURRENCY_API_KEY')
#         self.weather_api_key = os.getenv('WEATHER_API_KEY', 'YOUR_WEATHER_API_KEY')
#         self.stock_api_key = os.getenv('STOCK_API_KEY', 'YOUR_STOCK_API_KEY')

#     def test_currency_conversion_live(self):
#         """Test currency conversion with live data."""
#         response = self.client.get(self.currency_url, {
#             'base_currency': 'USD',
#             'target_currency': 'EUR',
#             'amount': 100
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('converted_amount', response.data)
#         self.assertIn('rate', response.data)
#         self.assertGreater(response.data['converted_amount'], 0)

#     def test_weather_live(self):
#         """Test weather endpoint with live data."""
#         response = self.client.get(self.weather_url, {'city': 'London'})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('main', response.data)
#         self.assertIn('temp', response.data['main'])

#     def test_stock_price_live(self):
#         """Test stock price endpoint with live data."""
#         response = self.client.get(self.stock_url, {'symbol': 'AAPL'})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('prices', response.data)
#         self.assertIn('1. open', response.data['prices'])
