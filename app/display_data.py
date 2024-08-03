
from weather_api import get_weather



def display_data(city):
    '''
    display data from api
    parameters passed: city by default
    
    '''

    weather_data = get_weather(city)

    return weather_data


def display_temp(weather_data,city):

    '''
    display temperature
    returns temperature in celsius
    
    '''

    display_temp = weather_data['main']['temp']

    print(f'Current temperature for {city} is {display_temp}°C')




# def display
