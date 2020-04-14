import requests
import json

def addAuction(auctionItem, token):
    url = 'http://172.31.47.107:9999/newAuction/auction/add/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    json_response = response.json()
    print(json_response)

auctionItem1 = {
    "title": "monday item",
    "endDate": "2020-04-06T22:00:00Z",
    "price": 1,
  	"description": "for work done on monday night"
}

token = 'UH80T43UJ67LgWqFkrm0fb1NjVcrG6'

addAuction(auctionItem1, token)