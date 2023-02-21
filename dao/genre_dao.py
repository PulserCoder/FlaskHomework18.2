from dao.model.genre import Genre
from dao.model.genre import GenreSchema

class GenreDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return Genre.query.all()

    def get_one(self, did):
        return Genre.query.get(did)

