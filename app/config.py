from dotenv import load_dotenv
import os

load_dotenv()



BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

def read_api_key():
    api_key = os.getenv('OPEN_WEATHER_API_KEY')

    if not api_key:
        print('key not found')
        exit()
    return api_key

