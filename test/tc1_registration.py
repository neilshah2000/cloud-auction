import requests

def createUser(user):
    url = 'http://172.31.47.107:9999/authentication/register/'
    response = requests.post(url, data = user)
    json_response = response.json()
    print(json_response)


users = [
    {'username': 'olga', 'password': 'olga'},
    {'username': 'nick', 'password': 'nick'},
    {'username': 'mary', 'password': 'mary'}
]

for user in users:
    createUser(user)