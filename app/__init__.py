"""Инициализация Flask"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
app = Flask(__name__)
login = LoginManager(app)


def create_app():
    app.config.from_object(Config)

    db.init_app(app)

    from app import routes
    return app