import json
import requests



def get_current_weather():
    # API url
    url = "http://api.openweathermap.org/data/2.5/weather?q=Odessa,ua&units=metric&APPID=888f6def0b40b79bce8c0cf3ebd774d6"
    # Get request for API
    response = requests.get(url)
    # Parse JSON data
    data = json.loads(response.text)
    # Weather init
    weather = 'Город: ' + data['name'] + '\n' \
                + 'Температура: ' + str(data['main']['temp']) + ' °C' + '\n' \
                + 'Влажность: ' + str(data['main']['humidity']) + ' %' + '\n'\
                + 'Давление: ' + str(data['main']['pressure']) + ' кПа' + '\n'\
                + 'Облачность: ' + str(data['clouds']['all']) + ' %' + '\n'\
                + 'Скорость ветра: ' + str(data['wind']['speed']) + ' м/c' + '\n'
    return weather
