import requests
import json
from getAllItems import getAllItems
from login import loginUser

mary = {'username': 'mary', 'password': 'mary'}
maryToken = loginUser(mary)

response = getAllItems( maryToken)

myJson = response.text
parsed = json.loads(myJson)
print(json.dumps(parsed, indent=4, sort_keys=True))