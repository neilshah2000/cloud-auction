import requests
import json
from datetime import datetime, timedelta


# User is object like {'username': 'olga', 'password': 'olga'}
def loginUser(user):
    url = 'http://172.31.47.107:9999/authentication/token/'
    response = requests.post(url, data = user)
    json_response = response.json()
    return json_response['access_token']


def addBid(auctionId, amount, token):
    auctionItem = {
        "amount": amount,
        "item": auctionId
    }
    url = 'http://172.31.47.107:9999/newAuction/bid/add/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    return response


def getBids(auctionItemId, token):
    url = 'http://172.31.47.107:9999/newAuction/getBidsForItem/' + str(auctionItemId)
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def getItem(itemId, token):
    url = 'http://172.31.47.107:9999/v1/auctionItem/' + str(itemId)
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def getAllItems(token):
    url = 'http://172.31.47.107:9999/v1/auctionItem/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def getSoldItems(token):
    url = 'http://172.31.47.107:9999/newAuction/auction/sold/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


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