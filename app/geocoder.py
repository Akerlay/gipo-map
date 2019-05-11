import requests
from app.config import Config


config = Config()


class Coords:
    def __init__(self, latitude: str, longitude: str, title: str):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title

    def __str__(self):
        return f'Coords(latitude={self.latitude}, longitude={self.longitude})'


class Geocoder:
    BASE_URL = 'https://geocode-maps.yandex.ru/1.x/'

    @staticmethod
    def get_coords(city_title: str) -> Coords:
        city_gobj = requests.get(f'{Geocoder.BASE_URL}'
                                 f'?geocode={city_title}'
                                 f'&apikey={config["YANDEX_GEOCODER_KEY"]}'
                                 '&format=json')
        resp_json_payload = city_gobj.json()
        point = resp_json_payload['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        title = resp_json_payload['response']['GeoObjectCollection']['featureMember'][0] \
            ['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
        lon, lat = point.split(' ')
        return Coords(lat, lon, title)

    def get_title(self, lat, lon):
        city_gobj = requests.get(f'{self.BASE_URL}'
                                 f'?geocode={lat},{lon}'
                                 f'&apikey={config["YANDEX_GEOCODER_KEY"]}'
                                 '&kind=locality'
                                 '&sco=latlong'
                                 '&format=json')
        resp_json_payload = city_gobj.json()
        point = resp_json_payload['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        title = resp_json_payload['response']['GeoObjectCollection']['featureMember'][0] \
            ['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
        lon, lat = point.split(' ')
        return Coords(lat, lon, title)
