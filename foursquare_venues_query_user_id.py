import requests
import json


def foursquare_query_user_id(client_id_path, client_secret_path, user_id_path, VERSION):

    x = open(client_id_path,"r")

    CLIENT_ID = x.readlines()[0]    

    y = open(client_secret_path,"r")

    CLIENT_SECRET = y.readlines()[0]

    z = open(user_id_path,"r")

    id_user = z.readlines()[0]

    
    url="https://api.foursquare.com/v2/users/{}?client_id={}&client_secret={}&v={}".format(id_user, CLIENT_ID, CLIENT_SECRET, VERSION)


    return json.dumps(requests.get(url).json(), indent=2)

if __name__ == '__main__':

    print(foursquare_query_user_id('CLIENT_ID.txt','CLIENT_SECRET.txt','foursquare_user.txt', "20170422"))

    