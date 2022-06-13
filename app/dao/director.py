# CRUD
from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return Director.query.get(did)

    def get_all(self):
        return Director.query.all()

