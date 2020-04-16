import requests
import json

def addAuction(auctionItem, token):
    url = 'http://172.31.47.107:9999/newAuction/auction/add/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    json_response = response.json()
    print(json_response)

auctionItem1 = {
    "title": "Thursday item",
    "endDate": "2020-04-16T18:30:00Z", # Server timestamp is one hour behind ours
    "price": 1,
  	"description": "for work done on Thursday night"
}

token = 'CXcx3feNq8U0VHOcLzRqhAP9x9OPqo'

addAuction(auctionItem1, token)