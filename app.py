from flask import Flask
from flask_restx import Api
from views.films import film_ns
from views.genres import genre_ns
from views.directors import director_ns
from config import Config
from setup_db import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(film_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)



app = create_app(Config())
app.debug = True
with app.app_context():
    db.create_all()
    db.session.commit()
if __name__ == '__main__':
    app.run(debug=True)
