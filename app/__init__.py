from flask import Flask

from app.config import Config

REQUIRED_CONFIG_FIELDS = ['CSRF_ENABLED', 'SECRET_KEY', 'YANDEX_WEATHER_KEY', 'YANDEX_GEOCODER_KEY', 'OWM_KEY']
CONFIG_PATH = 'config.json'
config = Config(CONFIG_PATH, REQUIRED_CONFIG_FIELDS)




app = Flask(__name__)
app.config.from_object(config)

from app import views
