from dao.model.movies import Movie


class MoviesDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, director_id, genre_id, year):
        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id)
        elif genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id)
        elif year:
            movies = Movie.query.filter(Movie.year == year)
        else:
            movies = Movie.query.all()
        return movies

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, data):
        mid = data.get('id')

        movie = Movie.query.get(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.session.add(movie)
        self.session.commit()
        # self.session.close()
        return movie


    def update_partial(self, data):
        pass

    def delete(self, mid):
        movie = self.session.query(Movie).get(mid)
        self.session.delete(movie)
        self.session.commit()


