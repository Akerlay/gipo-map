import requests
from app.geocoder import Geocoder, Coords
from app.config import Config
import json


config = Config()


class OpenWeatherAdapter:
    def __init__(self):
        self.geocoder = Geocoder()

    def get_forecast(self, lat, lon):
        real_pos = self.geocoder.get_title(lat, lon)
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?lat={real_pos.latitude}'
            f'&lon={real_pos.longitude}&units=metric&lang=ru&appid=' + config['OWM_KEY'])
        print(json.dumps(response.json()))
        print(type(response.json()))
        return self._convert_to_fc(real_pos, response.json())

    @staticmethod
    def _convert_to_fc(coords, resp_json):
        temp = round(resp_json['main']['temp'])
        return {
            'lat': coords.latitude,
            'lon': coords.longitude,
            'temp': str(temp) if temp <= 0 else '+' + str(temp),
            'pressure': int(resp_json['main']['pressure'] * 0.750062),
            'humidity': resp_json['main']['humidity'],
            'wind_speed': resp_json['wind']['speed'],
            'title': coords.title,
            'icon': 'http://openweathermap.org/img/w/' + resp_json['weather'][0]['icon'] + '.png'

        }
