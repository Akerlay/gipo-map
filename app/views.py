from flask import render_template, flash, redirect, jsonify
from app import app
# from app.forms import CityForm
from app.adapters import Adapter, YandexWeatherAdapter


weather_api: Adapter = YandexWeatherAdapter()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('mappa.html', data={1})


@app.route('/get-weather', methods=['POST'])
def get_weather():
    cities = ['Екатеринбург', 'Киев', 'Москва', 'Новосибирск', 'Владивосток', 'Челябинск', 'Златоуст', 'Новоуральск']
    res = []
    for city in cities:
        res.append(weather_api.get_forecast_title(city)[1])

    return jsonify(res)



# [{'title': 'Москва', 'lat': 55.723946, 'lon': 37.618932, 'temp': 20},
#                     {'title': 'Екатеринбург', 'lat': 56.833891, 'lon': 60.603227, 'temp': 40}]