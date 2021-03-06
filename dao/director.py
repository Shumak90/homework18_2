from dao.model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        pass

    def update(self, data):
        pass

    def update_partial(self, data):
        pass

    def delete(self, did):
        pass

