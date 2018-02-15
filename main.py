'''Mango Kasha: Dasha Shifrina, Karina Ionkina

SoftDev2 pd7

K #04: Mi only nyam ital food, mon!

2018-02-15  '''  


from pymongo import MongoClient
from hashlib import sha1
import shutil

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
