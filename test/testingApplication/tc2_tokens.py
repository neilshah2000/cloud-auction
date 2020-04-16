import requests
import json
from login import loginUser

users = [
    {'username': 'olga', 'password': 'olga'},
    {'username': 'nick', 'password': 'nick'},
    {'username': 'mary', 'password': 'mary'}
]

for user in users:
    token = loginUser(user)
    print(user['username'] + ' is logged in with token ' + token)