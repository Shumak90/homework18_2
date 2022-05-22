from flask_restx import Resource, Namespace

from container import genre_dao
from dao.model.genre import genres_schema, genre_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_dao.get_all
        genre_json = genres_schema.dump(genres)
        return genre_json, 200


@genre_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        genre = genre_dao.get_one(gid)
        director_json = genre_schema.dump(genre)
        return director_json, 200