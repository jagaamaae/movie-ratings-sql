from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title,
                  overview=overview,
                  release_date=release_date,
                  poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movies():
    """Return all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    movie_id=Movie.query.get(movie_id)
    return movie_id

def get_users():
    return User.query.all()

def get_user_email(email):
    user_email=User.query.filter_by(email=email).first()
    return user_email 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)