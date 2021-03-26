"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import User, connect_to_db
import crud
# Replace this with routes and view functions!

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/movies')
def show_movies():
    movies = crud.get_movies()
    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_details(movie_id):
    movie=crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def show_users():
    users = crud.get_users()
    return render_template('users.html', users=users)

@app.route('/users/<email>')
def show_users_details(email):
    user=crud.get_user_email(email)
    return render_template('user_details.html', users=user)

@app.route("/users", methods = ["POST"])
def register_user():
    email=request.form.get('email')
    password=request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')
    
@app.route("/login-info", methods = ['POST'])
def login_info():
    email=request.form.get('email')
    password=request.form.get('password')
    session['email'] = crud.get_user_by_email(email)
    session['password']= crud.get_user_by_email(email)
    if email == session['email'] and password == session['password']:
        flash('Logged in!') 
    else:
        flash("Either email or password don't match")
    return redirect('/')
    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)