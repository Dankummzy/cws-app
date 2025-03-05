import requests
import logging

API_KEY = '7275a1bd9bac87d9e9988cd882587a2b'
BASE_URL = 'https://api.exchangeratesapi.io/v1/latest'

def fetch_exchange_rates():
    try:
        response = requests.get(BASE_URL, params={
            'access_key': API_KEY,
        })
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        logging.debug(f"Exchange rates fetched: {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching exchange rates: {e}")
        return {'error': str(e)}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {'error': 'Unexpected error occurred'}