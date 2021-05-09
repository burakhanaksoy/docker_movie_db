from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse
from flask_migrate import Migrate
from my_function import pairs

app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/movie_db'
# app.debug = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Movies(db.Model):
    __tablename__ = 'movies'

    mov_title = db.Column(db.String(200), primary_key=True)
    mov_time = db.Column(db.Integer(), nullable=False, default=0)

    def __init__(self, mov_title, mov_time):
        self.mov_title = mov_title
        self.mov_time = mov_time

    def __repr__(self):
        return f'{self.mov_title} {self.mov_time}'


@app.route('/test', methods=['GET'])
def index():
    return {'test': 'test1'}


@app.route('/movies', methods=['GET'])
def get_all_movies():
    all_movies = Movies.query.all()
    movies = {}
    output = []
    for m in all_movies:
        movie = {}
        movie['title'] = m.mov_title
        movie['length'] = m.mov_time
        output.append(movie)
    movies['movies'] = output
    return jsonify(movies)


@app.route('/flight/movies')
def get_movies():
    parser = reqparse.RequestParser()
    parser.add_argument('duration', type=int, help='invalid time')
    args = parser.parse_args()
    duration = args['duration']

    movies_sorted_by_length = Movies.query.filter(
        Movies.mov_time < duration).order_by(Movies.mov_time).all()
    ordered_mov_time = []
    for i in range(len(movies_sorted_by_length)):
        ordered_mov_time.append(movies_sorted_by_length[i].mov_time)

    mov_tuple = (*pairs(ordered_mov_time, duration),)
    output = []
    movie_dict = {}
    for mov_pairs in mov_tuple:
        a, b = mov_pairs
        movie1 = Movies.query.filter(Movies.mov_time == a).first()
        movie2 = Movies.query.filter(Movies.mov_time == b).first()
        movie1_dict = {}
        movie1_dict['title'] = movie1.mov_title
        movie1_dict['length'] = movie1.mov_time
        movie2_dict = {}
        movie2_dict['title'] = movie2.mov_title
        movie2_dict['length'] = movie2.mov_time
        movie3_dict = {}
        movie3_dict['movie1'] = movie1_dict
        movie3_dict['movie2'] = movie2_dict
        output.append(movie3_dict)

    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
