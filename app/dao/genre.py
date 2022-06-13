# CRUD
from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return Genre.query.get(gid)

    def get_all(self):
        return Genre.query.all()
