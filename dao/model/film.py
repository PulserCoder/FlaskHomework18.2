from marshmallow import fields, Schema
from sqlalchemy.orm import relationship

from setup_db import db


class Film(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    trailer = db.Column(db.String())
    year = db.Column(db.Integer())
    rating = db.Column(db.String())
    genre_id = db.Column(db.Integer(), db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer(), db.ForeignKey('directors.id'))
    genres = relationship('Genre')
    directors = relationship('Director')


class FilmSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.String()
    genre_id = fields.Integer()
    director_id = fields.Integer()
