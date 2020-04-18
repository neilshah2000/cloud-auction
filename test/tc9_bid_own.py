import requests
import json
from helpers import addBid, loginUser


user = {'username': 'mary', 'password': 'mary'}
token = loginUser(user)


maryAuctionId = 48
amount = 56

response  = addBid(maryAuctionId, amount, token)

print(response.json())