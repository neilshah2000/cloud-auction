import requests
import json
from helpers import getSoldItems, loginUser, getItem


mary = {'username': 'mary', 'password': 'mary'}
maryToken = loginUser(mary)

response = getSoldItems(maryToken)

myJson = response.text
parsed = json.loads(myJson)
print(json.dumps(parsed, indent=4, sort_keys=True))