from flask import Flask
from app.views import configure as set_bp
import os


def create_app():
    app = Flask(__name__)
    set_bp(app)

    return app
