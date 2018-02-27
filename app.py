from flask import Flask, session, url_for, redirect, render_template, request
import main
from main import *
import os
import urllib2
import json

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods = ['GET', 'POST'])
def main():
    genres = []
    genres = all_genres()
#    print genres
    return render_template('index.html', genres = genres)


@app.route("/respond", methods = ['GET', 'POST'])
def respond():
    #if request.method=="POST":
    print "ya"
    query = float(request.args['query'])
    print query
    if (query == 1):
        year = request.args['year']
        ret = []
        ret = get_movies(year)
        return render_template('respond.html', result = ret)
    elif (query == 2):
        actor = request.args['actor']
        ret = []
        ret = get_starred_films(actor)
        return render_template('respond.html', result = ret)
    elif (query == 3):
        director = request.args['director']
        ret = []
        ret = get_director_films(director)
        return render_template('respond.html', result = ret)
    elif (query == 4):
        year = request.args['year']
        genre = request.args['genre']
        ret = []
        ret = genre_year(genre, year)
        return render_template('respond.html', result = ret)
    elif (query == 5):
        year = request.args['year']
        ret = []
        ret = movies_past_year(year)
        return render_template('respond.html', result = ret)
    elif(query ==6):
        title = request.args['title']
        print "movie title"
        ret = []
        ret = movie_info(title)
        return render_template('respond.html', result = ret)
    else:
        print "not get"
        return render_template('index.html')



if __name__ == "__main__":
    app.debug = True
    app.run()
