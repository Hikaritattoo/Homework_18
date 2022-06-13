from flask import request, jsonify
from flask_restx import Resource, Namespace
from app.container import movie_service
from app.dao.model.movie import MovieSchema


movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        year = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if year:
            movie = movie_service.get_by_year(year)
        elif director_id:
            movie = movie_service.get_by_director_id(director_id)
        elif genre_id:
            movie = movie_service.get_by_genre_id(genre_id)
        else:
            movie = movie_service.get_all()
        return movies_schema.dump(movie), 200

    def post(self):
        data = request.get_json()
        movie_service.create(data)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        movie_service.update(req_json, mid)
        return '', 204

    def patch(self, mid):
        req_json = request.json
        movie_service.update_partial(req_json, mid)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
