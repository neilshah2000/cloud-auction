import requests
import json

def addBid(auctionItem, token):
    url = 'http://172.31.47.107:9999/newAuction/bid/add/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    status = response.status_code
    print(status)
    json_response = response.json()
    print(json_response)

maryBid = {
    "amount": 70,
    "time": "2020-03-13T10:10:00Z",
    "item": 3
}

token = 'UH80T43UJ67LgWqFkrm0fb1NjVcrG6'

addBid(maryBid, token)