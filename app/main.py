from display_data import display_data, display_temp


def main():
    city = 'London'
    weather_data = display_data(city)
    if weather_data:
        display_temp(weather_data, city)
    else:
        print(f"Failed to retrieve weather data for {city}.")
    




if __name__ == '__main__':

    main()