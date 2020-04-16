import requests
import json
from login import loginUser

def addBid(auctionItem, token):
    url = 'http://172.31.47.107:9999/newAuction/bid/add/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    status = response.status_code
    print(status)
    json_response = response.json()
    print(json_response)

########## config ##############

maryBid = {
    "amount": 70,
    "time": "2020-03-13T10:10:00Z",
    "item": 3
}

user = {'username': 'mary', 'password': 'mary'}
token = loginUser(user)

addBid(maryBid, token)