from flask import render_template, flash, redirect, jsonify, request
from app import app
# from app.forms import CityForm
from app.adapters import OpenWeatherAdapter


owm = OpenWeatherAdapter()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('mappa.html', data={1})


@app.route('/get-weather', methods=['POST'])
def get_weather():
    args = request.form
    # response = jsonify(owm.get_forecast(args['lat'], args['lon']))
    response = jsonify({'lat': args['lat'],
            'lon': args['lon'],
            'temp': '+12',
            'pressure': int(1000 * 0.750062),
            'humidity': 67,
            'wind_speed': 2,
            'title': 'Жмыхово',
            'icon': 'https://lastfm-img2.akamaized.net/i/u/ar0/3829e26e3d8edc9e947a130564e01134.png'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
