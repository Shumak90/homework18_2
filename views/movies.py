from flask import request
from flask_restx import Resource, Namespace

from container import movie_dao
from dao.model.movies import movies_schema, movie_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        movies = movie_dao.get_all(director_id, genre_id, year)
        movies_json = movies_schema.dump(movies)
        return movies_json, 200

    def post(self):
        data = request.json
        movie_dao.create(data)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        try:
            movie = movie_dao.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return '', 404

    def put(self, mid: int):
        data = request.json
        data['id'] = mid
        movie_dao.update(data)
        return '', 204

    def delete(self, mid: int):
        movie_dao.delete(mid)
        return '', 204