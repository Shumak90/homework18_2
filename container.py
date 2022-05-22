from dao.director import DirectorDao
from dao.genre import GenreDao
from dao.movies import MoviesDao
from setup_db import db

movie_dao = MoviesDao(db.session)
genre_dao = GenreDao(db.session)
director_dao = DirectorDao(db.session)