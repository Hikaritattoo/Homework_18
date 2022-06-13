# CRUD
from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return Movie.query.all()

    def get_one(self, mid):
        return Movie.query.get(mid)

    def get_by_year(self, year):
        movie = Movie.query.filter(Movie.year == year).all()
        return movie

    def get_by_director_id(self, director_id):
        movie = Movie.query.filter(Movie.director_id == director_id).all()
        return movie

    def get_by_genre_id(self, genre_id):
        movie = Movie.query.filter(Movie.genre_id == genre_id).all()
        return movie

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
