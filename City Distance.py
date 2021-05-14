# -*- coding: utf-8 -*-
'''
Calculates the distance between two cities
'''

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="user")

def distance(city1,city2,unit):
    location1 = geolocator.geocode(city1)
    location2 = geolocator.geocode(city2)
    coor1 = (location1.latitude, location1.longitude)
    coor2 = (location2.latitude, location2.longitude)
    if unit == "km":
        distances = geodesic(coor1, coor2).km
    elif unit == "miles":
        distances = geodesic(coor1, coor2).miles
        
    print(f"The distance between {city1} and {city2} is {distances:.4f} {unit}")
    
def main():
    print("Type in the name of two cities, and choose the unit of distance")
    city1 = input("City 1: ")
    city2 = input("City 2: ")
    unit = input("Distance in 'miles' or 'km': ")
    distance(city1, city2, unit)
    
if __name__ == "__main__":
    main()