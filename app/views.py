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
    response = jsonify(owm.get_forecast(args['lat'], args['lon']))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
