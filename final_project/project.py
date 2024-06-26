from geopy import distance
from geopy.geocoders import Nominatim
def main():
    number=int(input("How many cities are you visiting? "))
    print("Consider that the starting point is the first city entered.")
    cities, final_route= cities_list(number)
    position=cities[0]
    final_route[0]=position
    cities[0]="Visited"
    aux_route=aux()
    distance=0
    while aux_route<number:
        minor_distance=float("inf")
        for x in range(number):
            if cities[x]=="Visited":
                pass
            else:
                next=cities[x]
                if distance_to_km(coordinate(position),coordinate(next))<minor_distance:
                    minor_distance=distance_to_km(coordinate(position),coordinate(next))
                    aux_position=x
        final_route[aux_route]=cities[aux_position]
        position=cities[aux_position]
        cities[aux_position]="Visited"
        aux_route+=1
        distance+=minor_distance
    print(f"Final route: {final_route}")
    print(f"Final distance: {distance} km")

def cities_list(number):
    cities=[]
    final_route=[]
    for i in range (number):
        city=input("Type the cities you are visiting: ")
        cities.append(city)
        final_route.append(0)
    return cities, final_route

def aux():
    return 1
def coordinate(city):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(f"{city}")
    return [location.latitude, location.longitude]

def distance_to_km(x1,x2):
    return round(distance.distance(x1,x2).km)

if __name__=="__main__":
    main()
