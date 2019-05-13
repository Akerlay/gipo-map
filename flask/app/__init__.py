from flask import Flask


app = Flask(__name__)
app.config.from_mapping({"CSRF_ENABLED": True, "SECRET_KEY": "forSquaRea551574nc3"})

from app import views
