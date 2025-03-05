import requests

API_KEY = '09675cafdebf3d4320e62a5252c85a4e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city_name):
    response = requests.get(f'{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric')
    if response.status_code == 200:
        return response.json()
    return None
