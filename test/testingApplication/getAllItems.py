import requests
import json

def getAllItems(token):
    url = 'http://172.31.47.107:9999/v1/auctionItem/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response