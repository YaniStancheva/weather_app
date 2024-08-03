import requests
from config import read_api_key, BASE_URL



def get_weather(city):
    api_key = read_api_key()
    url = f'{BASE_URL}q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed -> {e}")
        return None
