from dao.director_dao import DirectorDAO
from dao.model.director import DirectorSchema

class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao
        self.director_schema = DirectorSchema()
        self.directors_schema = DirectorSchema(many=True)

    def get_all(self):
        directors = self.dao.get_all()
        return self.directors_schema.dump(directors)

    def get_one(self, uid):
        director = self.dao.get_one(uid)
        return self.director_schema.dump(director)