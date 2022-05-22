from dao.genre import GenreDao


class GenreServices:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        pass

    def update(self, data):
        pass

    def update_partial(self, data):
        pass

    def delete(self, did):
        pass

