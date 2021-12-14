################################################################################################
##     DEPENDENCIES
################################################################################################
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

################################################################################################
##     # POSTGRES DATABASE  CREDENTIALS
################################################################################################
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

app = Flask(__name__)

################################################################################################
## # CORS IMPLEMENTED SO AS NOT  TO GET ANY  ERRORS  WHEN  ACCESSING  THE  SERVER
################################################################################################
CORS(app)

try:
    con = psycopg2.connect(
        database=DATABASE,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD)

    cur = con.cursor()

################################################################################################
###                             ROUTES  
################################################################################################
    # Fetching all movies from the database
    @app.route('/')
    def fetch_all_movies():
        cur.execute('SELECT * FROM movies')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)

    #Fetching movies by movieId from the database
    @app.route('/<int:movie_id>')
    def fetch_by_id(movie_id=None):
        cur.execute(f'SELECT * FROM movies WHERE movie_id = {movie_id}')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)

    # Creating movies and adding  them to the database
    @app.route('/add-movie', methods=['GET', 'POST'])
    def add_movie():
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            cur.execute("INSERT INTO movies (movie_name, img_url, release_year, summary, director, genre, rating, movie_runtime, meta_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (f"{data['movieName']}", f"{data['imgUrl']}", data['releaseYear'], f"{data['summary']}",
                         f"{data['director']}", f"{data['genre']}", f"{data['rating']}", data['movieRuntime'], data['metaScore']))
            con.commit()
            return 'Form submitted'
        else:
            return 'Form submission failed'

    # Deleting a  movie by movieId from the database
    @app.route('/delete-movie', methods=['GET', 'DELETE'])
    def delete_by_id():
        movie_id = request.form.to_dict()
        print(movie_id['movieId'])
        cur.execute(
            f"DELETE FROM movies WHERE movie_id = {movie_id['movieId']} RETURNING movie_name")
        con.commit()

        return 'Movie Deleted'

    #Updating movie by movieId from the database
    @app.route('/update-movie', methods=['GET', 'PUT'])
    def update_by_id():

        cur.execute(
            'UPDATE movies SET movie_name = \'Goldeneye\' WHERE movie_id = 1')
        con.commit()

        return 'Movie Updated'

except:
    print('Error')
