import json
from helpers import getAllAvailableItems, loginUser, getItem


nick = {'username': 'nick', 'password': 'nick'}
nickToken = loginUser(nick)

response = getAllAvailableItems(nickToken)

myJson = response.text
parsed = json.loads(myJson)
print(json.dumps(parsed, indent=4, sort_keys=True))