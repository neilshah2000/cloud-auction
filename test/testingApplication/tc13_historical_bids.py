import requests
import json
from helpers import getBids, loginUser, getItem


mary = {'username': 'mary', 'password': 'mary'}
maryToken = loginUser(mary)

nick = {'username': 'nick', 'password': 'nick'}
nickToken = loginUser(nick)

# Mary can view her own historical bids
response = getBids(30, maryToken)
myJson = response.text
parsed = json.loads(myJson)
print(json.dumps(parsed, indent=4, sort_keys=True))


# Nick can not view mary's historical bids
response = getBids(30, nickToken)
myJson = response.text
parsed = json.loads(myJson)
print(json.dumps(parsed, indent=4, sort_keys=True))