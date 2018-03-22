from flask import jsonify
from . import service
from app.models import Movie
from app import db

@service.route('/movie/<id>/')
def main(id):
    movie = Movie.query.filter_by(movieid=id).first()
    return jsonify({
        "comment": movie.bigComment,
        'rate1': movie.rate1,
        "rate2": movie.rate2,
        "rate3": movie.rate3,
        "rate4": movie.rate4
    })
