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

client_id = 'UjHGNXR1QL1xcz1hqzWDpQYZnjbRT5KJX96t4xQL'
client_secret = 'NIEapuwf7PX0qF5B8laufp60CAQHI0KWW6wsywKjnh9Xb5qyLKTPzGoLzk4bcFD46HCnm3MlVWi4tN5pKeFip33qtXpiVATcIDfM1ScUEv4LbG4s2dQZBMkeYQ43QqZL'