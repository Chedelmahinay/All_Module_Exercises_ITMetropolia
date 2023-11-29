import requests


def get_weather(api_key, city_name):
    request = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city_name, 'appid': api_key}

    try:
        response = requests.get(request, params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city_name}: {data['weather'][0]['description']}")
            print(f"Temperature: {data['main']['temp'] - 273.15:.2f} °C")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"ERROR {e}")


city_name = input("Enter municipality name: ")
api_key = '6585a5b86f8872158cf5946c470a6488'
get_weather(api_key, city_name)
