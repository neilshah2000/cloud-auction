import requests
import json
from login import loginUser
from bid import addBid
from addItem import addAuctionItem

# get tokens
mary = {'username': 'mary', 'password': 'mary'}
maryToken = loginUser(mary)

olga = {'username': 'olga', 'password': 'olga'}
olgaToken = loginUser(olga)

nick = {'username': 'nick', 'password': 'nick'}
nickToken = loginUser(nick)

# mary creates item
minutesToEnd = 1
maryAddItemResponse = addAuctionItem('new item', 'item description', minutesToEnd, maryToken)
maryAddItemId = maryAddItemResponse.json()['id']


# olga bids on item
olgaResponse1 = addBid(maryAddItemId, 70, olgaToken)
print('olgaResponse1: ')
print(olgaResponse1.json())

# nick bids on item
nickResponse1 = addBid(maryAddItemId, 71, nickToken)
print('nickResponse1: ')
print(nickResponse1.json())

# olga bids on item
olgaResponse2 = addBid(maryAddItemId, 567, olgaToken)
print('olgaResponse2: ')
print(olgaResponse2.json())

# nick bids on item
nickResponse2 = addBid(maryAddItemId, 129, nickToken)
print('nickResponse2: ')
print(nickResponse2.json())