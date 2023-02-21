from dao.genre_dao import GenreDAO
from dao.movie_dao import FilmDAO
from dao.director_dao import DirectorDAO
from service.film import FilmService
from service.director import DirectorService
from service.genre import GenreService
from setup_db import db
film_dao = FilmDAO(db.session)
film_service = FilmService(dao=film_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)