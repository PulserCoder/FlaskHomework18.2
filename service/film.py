from dao.model.film import FilmSchema
from dao.movie_dao import FilmDAO


class FilmService:
    def __init__(self, dao: FilmDAO):
        self.dao = dao
        self.film_schema = FilmSchema()
        self.films_schema = FilmSchema(many=True)

    def find_filter(self, data):
        if data.get('director_id'):
            return self.filter_by_director(data.get('director_id'))
        if data.get('genre_id'):
            return self.filter_by_genre(data.get('genre_id'))
        if data.get('year'):
            return self.filter_by_year(data.get('year'))
        else:
            return self.get_all()

    def get_one(self, fid):
        film = self.dao.get_one(fid)
        return self.film_schema.dump(film)

    def get_all(self):
        films = self.dao.get_all()
        return self.films_schema.dump(films)

    def add_movie(self, data):
        self.dao.create_movie(data)

    def update_film(self, data, fid):
        film = self.dao.get_one(fid)
        if data.get('title'):
            film.title = data.get('title')
        if data.get('description'):
            film.description = data.get('description')
        if data.get('trailer'):
            film.trailer = data.get('trailer')
        if data.get('year'):
            film.year = data.get('year')
        if data.get('rating'):
            film.rating = data.get('rating')
        if data.get('genre_id'):
            film.genre_id = data.get('genre_id')
        if data.get('director_id'):
            film.director_id = data.get('director_id')
        self.dao.update_info(film)

    def delete_film(self, uid):
        self.dao.delete_film(uid)

    def filter_by_year(self, year):
        films = self.dao.get_movies_by_year(year)
        return self.films_schema.dump(films)

    def filter_by_genre(self, genre_id):
        films = self.dao.get_genres_movie(genre_id)
        return self.films_schema.dump(films)

    def filter_by_director(self, director_id):
        films = self.dao.get_directors_movie(director_id)
        return self.films_schema.dump(films)
