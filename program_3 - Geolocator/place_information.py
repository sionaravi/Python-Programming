# Siona Ravi
# CSCI 236
# Oct 10, 2020
# Geolocation: place information
# 5hours
# A version
# I had to keep rewriting the program
# Status: It compiles very well

from geolocation import GeoLocation
class PlaceInformation:
    def __init__(self, name, address, tag, latitude, longitude):
        self.__name = name;
        self.__address = address;
        self.__tag = tag;
        self.__location = GeoLocation(latitude, longitude);
    def get_name(self):
        return self.__name;
    def get_address(self):
        return self.__address;
    def get_tag(self):
        return self.__tag;
    def __str__(self):
        return 'Name = '+ self.__name + ', Location = ' + str(self.__location);
    def get_location(self):
        return self.__location;
    def distance_from(self, spot):
        distance = self.get_location().compute_distance(spot.latitude, spot.longitude);
        return str(round(distance, 2)) + 'miles';
        # To display the distance in Kilometer, uncomment the next line
        #return str(round(distance, 2)) + 'kilometers';