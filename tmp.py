#!/usr/bin/python3
from models import *

all_places = {}
try:
    all_places = storage.all("Place")
except:
    all_places = storage.all(Place)

if len(all_places) == 0:
    try:
        all_places = storage.all(Place)
    except:
        all_places = storage.all("Place")

from sqlalchemy import inspect

for place in all_places.values():
    try:
        inspect(place)
    except:
        print("Unmapped place:", place)

places_by_name = {}

for p_id in all_places.keys():
    place = all_places[p_id]
    places_by_name[place.name] = place
print(places_by_name)

for p_name in sorted(places_by_name.keys()):
    place = places_by_name[p_name]
    print("place: {}".format(place.name))
    if place.amenities is None:
        continue
    amenities_names = []
    for amenity in place.amenities:
        amenities_names.append(amenity.name)
    
    for a_name in sorted(amenities_names):
        print("\tamenity: {}".format(a_name))
