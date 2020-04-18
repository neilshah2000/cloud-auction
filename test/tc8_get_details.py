import json
from helpers import getItem, loginUser, getItem


nick = {'username': 'nick', 'password': 'nick'}
nickToken = loginUser(nick)

olga = {'username': 'olga', 'password': 'olga'}
olgaToken = loginUser(olga)

itemId = 48


responseNick = getItem(itemId, nickToken)
responseOlga = getItem(itemId, olgaToken)

nickJson = responseNick.text
nickParsed = json.loads(nickJson)
print(json.dumps(nickParsed, indent=4, sort_keys=True))

olgaJson = responseOlga.text
olgaParsed = json.loads(olgaJson)
print(json.dumps(olgaParsed, indent=4, sort_keys=True))