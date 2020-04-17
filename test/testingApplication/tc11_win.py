import requests
import json
from helpers import getAllItems, loginUser, getItem


mary = {'username': 'mary', 'password': 'mary'}
maryToken = loginUser(mary)

response = getItem(30, maryToken)

myJson = response.text
parsed = json.loads(myJson)
print(json.dumps(parsed, indent=4, sort_keys=True))