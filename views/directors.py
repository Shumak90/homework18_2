from flask_restx import Resource, Namespace

from container import director_dao
from dao.model.director import directors_schema, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_dao.get_all
        directors_json = directors_schema.dump(directors)
        return directors_json, 200


@director_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did: int):
        director = director_dao.get_one(did)
        director_json = director_schema.dump(director)
        return director_json, 200