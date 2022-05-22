from dao.model.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        pass

    def update(self, data):
        pass

    def update_partial(self, data):
        pass

    def delete(self, did):
        pass

