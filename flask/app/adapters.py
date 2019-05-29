import requests
from app.geocoder import Geocoder, Coords
import json
import os
from app.caching import Cache


class OpenWeatherAdapter:
    def __init__(self):
        self.geocoder = Geocoder()
        self.cache = Cache(30*60)

    def get_forecast(self, lat, lon):
        real_pos = self.geocoder.get_title(lat, lon)
        key = f"{real_pos.latitude}-{real_pos.longitude}"
        cahced_value = self.cache.get(key)
        if cahced_value:
            return json.loads(cahced_value)

        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?lat={real_pos.latitude}'
            f'&lon={real_pos.longitude}&units=metric&lang=ru&appid=' + os.environ['OWM_KEY'])

        forecast = self._convert_to_fc(real_pos, response.json())
        self.cache.set(key, json.dumps(forecast))
        return forecast

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
