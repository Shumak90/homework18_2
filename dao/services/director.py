from dao.director import DirectorDao


class DirectorServices:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

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

