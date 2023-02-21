from flask_restx import Resource, Namespace
from implemented import film_service
from flask import request
film_ns = Namespace('films')


@film_ns.route('/<int:fid>')
class FilmView(Resource):
    def get(self, fid):
        return film_service.get_one(fid), 200

    def put(self, fid):
        req_ = request.json
        return film_service.update_film(req_, fid), 201

    def patch(self, fid):
        req_ = request.json
        return film_service.update_film(req_, fid), 201

    def delete(self, fid):
        return film_service.delete_film(fid), 204

@film_ns.route('/')
class FilmsView(Resource):
    def get(self):
        data = request.args
        return film_service.find_filter(data), 200

    def post(self):
        req_ = request.json
        return film_service.add_movie(req_), 201
