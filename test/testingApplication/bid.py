import requests
import json

def addBid(auctionId, amount, token):
    auctionItem = {
        "amount": amount,
        "item": auctionId
    }
    url = 'http://172.31.47.107:9999/newAuction/bid/add/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    return response