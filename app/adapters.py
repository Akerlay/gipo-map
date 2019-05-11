import requests
from app.geocoder import Geocoder, Coords
from app.config import Config
from typing import Tuple
from app import app
import json

config = Config()

# class Weather:
#     ICON_URL = 'https://yastatic.net/weather/i/icons/blueye/color/svg/'
#
#     def __init__(self, single_moment_data):
#         temp = single_moment_data['temp']
#         feels = single_moment_data['feels_like']
#         self.temp = (str(temp) if temp < 0 else '+' + str(temp) if temp > 0 else '0') + '°'
#         self.feels = (str(feels) if feels < 0 else '+' + str(feels) if feels > 0 else '0') + '°'
#         self.icon = self.ICON_URL + single_moment_data['icon'] + '.svg'
#         self.wind_speed = single_moment_data['wind_speed']
#         self.wind_dir = single_moment_data['wind_dir']
#         self.pressure = single_moment_data['pressure_mm']
#         self.humidity = single_moment_data['humidity']
#
#
# class DailyForecast:
#     def __init__(self, data: dict):
#         self.date = data['date']
#         self.day = Weather(data['parts']['day_short'])
#         self.night = Weather(data['parts']['night_short'])
#
#
# class Forecast:
#     def __init__(self, data: dict):
#         self.days = [DailyForecast(day) for day in data['forecasts']]
#
#     def __iter__(self):
#         return self.days.__iter__()


class Adapter:
    def get_forecast(self):
        raise NotImplementedError

    def get_forecast_title(self, city_title: str):
        raise NotImplementedError

    def get_forecast_coords(self, lat: str, lon: str):
        raise NotImplementedError


class YandexWeatherAdapter(Adapter):
    BASE_URL = 'https://api.weather.yandex.ru/v1/forecast'

    def get_forecast_title(self, city_title: str):
        coords = Geocoder.get_coords(city_title)
        return self._get_forecast(coords)

    def get_forecast_coords(self, lat: str, lon: str):
        coords = Coords(lat, lon, "test")
        return self._get_forecast(coords)

    def _get_forecast(self, coords: Coords):
        response = requests.get(f'{self.BASE_URL}?lat={coords.latitude}&lon={coords.longitude}&lang=ru_RU',
                                headers={'X-Yandex-API-Key': config['YANDEX_WEATHER_KEY']})
        return coords.title, self._convert_to_fc(response.json())

    @staticmethod
    def _convert_to_fc(resp_json):
        return {
            'lat': resp_json['info']['lat'],
            'lon': resp_json['info']['lon'],
            'temp': resp_json['fact']['temp'],
            'feels': resp_json['fact']['feels_like'],
            'icon': resp_json['fact']['icon'],
            'condition': resp_json['fact']['condition']
        }


class OpenWeatherAdapter(Adapter):
    def get_forecast(self):
        response = requests.get('http://api.openweathermap.org/data/2.5/box/city?bbox=28,68,58,56,7&appid=' + config['OWM_KEY'])
        print(json.dumps(response.json()))
        return [self._convert_to_fc(place) for place in response.json()['list']]

    @staticmethod
    def _convert_to_fc(resp_json):
        return {
            'lat': resp_json['coord']['Lat'],
            'lon': resp_json['coord']['Lon'],
            'temp': resp_json['main']['temp'],
            'title': resp_json['name']
        }

    def get_forecast_coords(self, lat: str, lon: str):
        raise NotImplementedError

    def get_forecast_title(self, city_title: str):
        raise NotImplementedError
