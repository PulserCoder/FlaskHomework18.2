from flask_restx import Resource, Namespace
from implemented import director_service
director_ns = Namespace('directors')


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        return director_service.get_one(did), 200


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return director_service.get_all(), 200
