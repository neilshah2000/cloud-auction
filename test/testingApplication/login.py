import requests
import json

# User is object like {'username': 'olga', 'password': 'olga'}
def loginUser(user):
    url = 'http://172.31.47.107:9999/authentication/token/'
    response = requests.post(url, data = user)
    json_response = response.json()
    return json_response['access_token']

