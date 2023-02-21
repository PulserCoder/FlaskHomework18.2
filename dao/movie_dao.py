from sqlalchemy.orm.scoping import ScopedSession

from dao.model.director import Director
from dao.model.film import Film
from dao.model.genre import Genre


class FilmDAO():
    def __init__(self, session: ScopedSession):
        self.session = session

    def get_one(self, fid) -> Film:
        return Film.query.get(fid)

    def get_all(self):
        return Film.query.all()

    def get_directors_movie(self, director_id):
        return Film.query.join(Director, Director.id == director_id).all()

    def get_genres_movie(self, genre_id):
        return Film.query.join(Genre, Genre.id == genre_id).all()

    def get_movies_by_year(self, year):
        return Film.query.filter(Film.year == year)

    def create_movie(self, data):
        new_book = Film(**data)
        self.session.add(new_book)
        self.session.commit()

    def update_info(self, film):
        self.session.add(film)
        self.session.commit()

    def delete_film(self, fid):
        self.session.delete(self.get_one(fid))
        self.session.commit()
