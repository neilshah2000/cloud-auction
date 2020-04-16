import requests
import json
from datetime import datetime, timedelta

def addAuctionItem(title, description, endsIn, token):
    auctionItem = createAuctionItemObject(title, description, endsIn)
    url = 'http://172.31.47.107:9999/newAuction/auction/add/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    return response

# helper method to create object the way the back end likes
def createAuctionItemObject(title, description, endsIn):
    endtime = datetime.now() + timedelta(minutes=endsIn)
    # endtime = endtime - timedelta(minutes=60) # Server timestamp is one hour behind ours
    myAuctionItem = {
        "title": title,
        "endDate": endtime.isoformat(),
        "price": 1,
        "description": description
    }
    return myAuctionItem

