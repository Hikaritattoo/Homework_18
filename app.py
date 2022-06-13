
from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


# функция создания основого объекта app


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application

# функция подключения расширений (SQLAlchemy, RESTX, ...etc)


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)


if __name__ == '__main__':
    app = create_app(Config())
    app.run()
