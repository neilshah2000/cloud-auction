import requests
import json
from helpers import getBids, loginUser, getItem


mary = {'username': 'mary', 'password': 'mary'}
maryToken = loginUser(mary)

response = getBids(30, maryToken)

myJson = response.text
parsed = json.loads(myJson)
print(json.dumps(parsed, indent=4, sort_keys=True))