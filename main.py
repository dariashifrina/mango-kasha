'''Mango Kasha: Dasha Shifrina, Karina Ionkina

SoftDev2 pd7

K #04: Mi only nyam ital food, mon!

2018-02-15  '''  

import requests, json

from pymongo import MongoClient
from hashlib import sha1
import shutil


#-------writing json file from link--------------------------------------------------------
filename = "black_mirror.json"
data = requests.get("http://api.tvmaze.com/singlesearch/shows?q=black-mirror&embed=episodes")
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
db.bm.insert(decoded)

def get_description(season, episode):
    episode = db.bm.find({"$and":[{"season": season}, {"number": episode}]})
    for i in episode:
        print i




get_description(4, 2)





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
