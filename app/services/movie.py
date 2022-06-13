from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def get_by_director_id(self, director_id):
        return self.dao.get_by_director_id(director_id)

    def get_by_genre_id(self, genre_id):
        return self.dao.get_by_genre_id(genre_id)

    def create(self, data):
        self.dao.create(data)

    def update(self, data, mid):
        movie = self.dao.get_one(mid)
        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        self.dao.update(movie)

    def update_partial(self, data, mid):
        movie = self.get_one(mid)
        if 'title' in data:
            movie.title = data['title']
        if 'director' in data:
            movie.director_id = data['director_id']
        if 'genre' in data:
            movie.director_id = data['genre_id']
        if 'year' in data:
            movie.director_id = data['year']
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
