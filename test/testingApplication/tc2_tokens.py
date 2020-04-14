import requests
import json

def loginUser(user):
    url = 'http://172.31.47.107:9999/authentication/token/'
    response = requests.post(url, data = user)
    json_response = response.json()
    print(json_response['access_token'])
    return json_response['access_token']

users = [
    {'username': 'olga', 'password': 'olga'},
    {'username': 'nick', 'password': 'nick'},
    {'username': 'mary', 'password': 'mary'}
]

for user in users:
    loginUser(user)