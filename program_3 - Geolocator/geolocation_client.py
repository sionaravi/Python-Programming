# Siona Ravi
# CSCI 236
# Oct 10, 2020
# Geolocation: geolocation_client
# 5hours
# A version
# I had to keep rewriting the program
# Status: It compiles very well

from geolocation import GeoLocation

def main():
stash = GeoLocation(34.988889, -106.614444)
ABQstudio = GeoLocation(34.989978, -106.614357)
FBIbuilding = GeoLocation(35.131281, -106.61263)

print("the stash is at ", stash.__str__())
print("ABQ stuido is at ", ABQstudio.__str__())
print("FBI building is at ", FBIbuilding.__str__())

print("distance in miles between:")
stash_studio = stash.distance_from(ABQstudio)
stash_fbi = stash.distance_from(FBIbuilding)

print(" stash/studio = ", stash_studio)
print(" stash/fbi = ", stash_fbi)

if __name__ == "__main__":
main()