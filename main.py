'''Mango Kasha: Dasha Shifrina, Karina Ionkina
SoftDev2 pd7
K #05: Import/Export Bank"
2018-02-25  '''  

'''
We used an American movies json file. 
For each movie it contains the movie:
- Title
- Director
- Year
- Cast
- Genre
- Notes

The download link is: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json 

Our import mechanism was using requests to write a json file, then read the file and use db.collection.insert(file_content)

Our functions are:
- get_movies(year)
- get_starred_films(actor)
- get_director_films(director)
- genre_year(genre, year)
- movies_past_year(year)
- movie_info(title)
'''

import requests, json
from pymongo import MongoClient
from hashlib import sha1
import shutil

#ascii errors
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#-------writing json file from link--------------------------------------------------------
filename = "movies.json"
data = requests.get("https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json")
data = (data.text)

f = open(filename, "w")
f.write(data)
f.close()
#------------------------------------------------------------------------------------------

#replace this with lisa server
client = MongoClient('lisa.stuy.edu', 27017)
#replace this with lisa database name and collection
db = client.test.movies
'''
file = open(filename, "r")
file = file.read()
decoded = json.loads(file)
#print decoded

#replace names 
db.mv.insert(decoded)
'''

def all_genres():
    genre = db.mv.find( { "genre" : { "$exists" : True } } );
    ret = []
    for i in genre:
        if i['genre'] not in ret:
            ret.append(i['genre'])
    return ret




def get_movies(year):
    '''
    prints a list of movies from the given year
    '''
    ret = []
    movies = db.mv.find({"year": year})
    for i in movies:
        if i['title'] not in ret:
            ret.append(i["title"])
    return ret

#returns a list of movies from 2014
#get_movies(2014)



def get_starred_films(actor):
    '''
    prints the year and title of films this actor
    was cast in
    '''
    films = db.mv.find({"cast": actor})
    ret = []
    for i in films:
        if i['title'] not in ret:
            ret.append(i["title"])
    return ret
        

#TO_DO: WHY IS THIS  NOT WORKING
#get_starred_films("Jennifer Lawrence")



def get_director_films(director):
    '''
    given director name, this fxn prints the title and year 
    of the director's movies
    '''
    films = db.mv.find({"director": director})
    ret = []
    for i in films:
        inner_ret = []
        if i['title'] not in ret:
            inner_ret.append(i['title'])
            inner_ret.append(i['year'])
        ret.append(inner_ret)
    return ret

#works but loops
#get_director_films("Quentin Tarantino")


def genre_year(genre, year):
    '''
    given a genre and a year, this returns movies
    that fulfill both requirements
    '''
    films = db.mv.find({"$and":[{"genre": genre}, {"year": year}]})
    ret = []
    for i in films:
        if i['title'] not in ret:
            ret.append(i["title"])
    return ret

#works but repeats
#genre_year("Crime", 1987)


def movies_past_year(year):
    '''
    prints a list of movies that were premiered past a certain year
    '''
    films = db.mv.find({"year": {"$gt": year}})
    ret = []
    for i in films:
        inner_ret = []
        if i['title'] not in ret:
            inner_ret.append(i['title'])
            inner_ret.append(i['year'])
        ret.append(inner_ret)
    return ret

#movies_past_year(2015)

def movie_info(title):
    '''
    given a movie title, this prints a list
    of information including the director,
    cast, and year
    '''
    film = db.mv.find_one({"title": title})
    ret = []
#    print "DIRECTOR: "
    ret.append(film['director'])
#    print "CAST: " 
    ret.append(film['cast'])
#    print "YEAR: "
    ret.append(film['year'])
    return ret

#movie_info("Pulp Fiction")


'''
client = MongoClient('lisa.stuy.edu', 27017)
restaurant = client.test.restaurants

def get_bor_restaurant(borough):
    places = restaurant.find({"borough": borough})
    for place in places:
        print place["name"] + ", ",
    return places

def get_zipgrade_restaurant(zipcode, grade):
    places = restaurant.find({"$and": [{"address.zipcode": zipcode}, {"grades.grade": grade}]})
    for place in places:
        print place["name"] + ", ",
    return places

def get_zip_restaurant(zipcode):
    places = restaurant.find({"address.zipcode": zipcode})
    for place in places:
        print place["name"] + ", ",
    return places

def get_zipscore_restaurant(zipcode, score):
    places = restaurant.find({"$and": [{"address.zipcode": zipcode}, {"grades.score": {"$lt": score }} ] })
    for place in places:
        print place["name"] + ", ",
    return places


#SPECIAL FXN
def get_cuisinezip_restaurant(cuisine, zipcode):
    places = restaurant.find({"$and": [{"address.zipcode": zipcode}, {"cuisine": cuisine} ] })
    for place in places:
        print place["name"] + " located at " + place["address"]["street"] + ", ",
    return places
 

print("getting restaurants in Brooklyn:")
get_bor_restaurant("Brooklyn")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("getting restaurants at zip 10282:")
get_zip_restaurant("10282")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("getting restaurants at zip 10282 with a rating of C:")
get_zipgrade_restaurant('10282', "C")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("getting restaurants at zip 10282 with a score below 10:")
get_zipscore_restaurant('10282', 10)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("finding Mexican restaurants at zip 10282:")
get_cuisinezip_restaurant("Mexican", "10282")
'''
