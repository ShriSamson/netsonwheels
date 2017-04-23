from geopy.geocoders import Nominatim
import requests
import json


def foursquare_query(client_id_path, client_secret_path, address, LIMIT, VERSION, SEARCH_QUERY):

    x = open(client_id_path,"r")

    CLIENT_ID = x.readlines()[0]    

    y = open(client_secret_path,"r")

    CLIENT_SECRET = y.readlines()[0]

    geolocator = Nominatim()
    location = geolocator.geocode(address)
    LATITUDE = location.latitude
    LONGITUDE = location.longitude
    
    url="https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&query={}&limit={}".format(CLIENT_ID, CLIENT_SECRET, LATITUDE, LONGITUDE, VERSION, SEARCH_QUERY, LIMIT)

    #results = requests.get(url).json()

    return json.dumps(requests.get(url).json(), indent=2)

if __name__ == '__main__':

    print(foursquare_query('CLIENT_ID.txt','CLIENT_SECRET.txt', "44 Tehama Street San Francisco CA", 30, "20170422", "Cofee"))