'''Mango Kasha: Dasha Shifrina, Karina Ionkina

SoftDev2 pd7

K #04: Mi only nyam ital food, mon!

2018-02-15  '''  

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
client = MongoClient('localhost', 27017)
#replace this with lisa database name and collection
db = client['test']


file = open(filename, "r")
file = file.read()
decoded = json.loads(file)
#print decoded

#replace names 
db.mv.insert(decoded)

def get_movies(year):
    movies = db.mv.find({"year": year})
    for i in movies:
        print i["title"]
    return movies

#returns a list of movies from 2014
#get_movies(2014)


#returns year and title of film the actor was cast in
def get_starred_films(actor):
    films = db.mv.find({"cast": actor})
    for i in films:
        print i["title"] 
    return films
#TO_DO: WHY IS THIS  NOT WORKING
#get_starred_films("Jennifer Lawrence")

def get_director_films(director):
    films = db.mv.find({"director": director})
    for i in films:
        print i['title']
    return films
#yay this works
get_director_films("Quentin Tarantino")



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
