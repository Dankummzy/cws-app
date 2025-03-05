import requests

API_KEY = 'L9TB4BMX4YOQM2BT'
BASE_URL = 'https://www.alphavantage.co/query'

def fetch_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return None
