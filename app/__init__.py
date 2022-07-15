from flask import Flask
from app.views import configure as set_bp
from app.aws_controller import put


def create_app():
    app = Flask(__name__)
    set_bp(app)
    put()
    return app
