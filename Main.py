import requests


def getWeatherTemp():
    city = input("City name")
    api_address = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=imperial&&apikey=004efc69e1c7010c6f3300fe896b35d5'

    url = api_address
    json_data = requests.get(url).json()
    temp = json_data['list'][0]['main']['temp']
    print(temp)

