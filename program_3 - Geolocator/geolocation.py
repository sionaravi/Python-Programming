# Siona Ravi
# CSCI 236
# Oct 10, 2020
# Geolocation: geolocation
# 5hours
# A version
# I had to keep rewriting the program
# Status: It compiles very well

# Calculate the distance (in km or in miles) bewteen two points on Earth, located by their latitude and longitude.
import haversine as hs
from haversine import Unit
class GeoLocation:
    def __init__(self, latitude, longitude):
        self.latitude = latitude;
        self.longitude = longitude;
        self.distance = 0;
    def compute_distance(self, latitude, longitude):
        loc1=(self.latitude, self.longitude);
        loc2=(latitude, longitude);
        # To display the distance in Kilometer, uncomment the next line
        #self.distance = hs.haversine(loc1,loc2,unit=Unit.METERS) /1000;
        self.distance = hs.haversine(loc1,loc2,unit=Unit.MILES);
        return self.distance;
    def __str__(self):
        return '(' + str(self.latitude) + ',' + str(self.longitude) + ')';
    