from dao.genre_dao import GenreDAO, GenreSchema
class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao
        self.genre_schema = GenreSchema()
        self.genres_schema =GenreSchema(many=True)

    def get_all(self):
        genres = self.dao.get_all()
        return self.genres_schema.dump(genres)

    def get_one(self, uid):
        genre = self.dao.get_one(uid)
        return self.genre_schema.dump(genre)