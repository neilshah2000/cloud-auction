import requests
import json

def browseAllAuctions(token):
    url = 'http://172.31.47.107:9999/v1/auctionItem/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    json_response = response.json()
    print(json_response)


token = 'UH80T43UJ67LgWqFkrm0fb1NjVcrG6'

browseAllAuctions(token)