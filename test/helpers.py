import requests
import json
from datetime import datetime, timedelta


serverUrl = 'http://54.173.178.23:9999/'


# User is object like {'username': 'olga', 'password': 'olga'}
def loginUser(user):
    url = serverUrl + 'authentication/token/'
    response = requests.post(url, data = user)
    json_response = response.json()
    return json_response['access_token']


def addBid(auctionId, amount, token):
    bid = {
        "amount": amount,
        "item": auctionId
    }
    url = serverUrl + 'auction/bid/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = bid)
    return response


def getBids(auctionItemId, token):
    url = serverUrl + 'auction/auctionItem/' + str(auctionItemId) + '/bids/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def getItem(itemId, token):
    url = serverUrl + 'auction/auctionItem/' + str(itemId)
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def getAllItems(token):
    url = serverUrl + 'auction/auctionItem/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def getAllAvailableItems(token):
    url = serverUrl + 'auction/auctionItem/available/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def getSoldItems(token):
    url = serverUrl + 'auction/auctionItem/sold/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    return response


def addAuctionItem(title, description, endsIn, token):
    auctionItem = createAuctionItemObject(title, description, endsIn)
    url = serverUrl + 'auction/auctionItem/'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(url, headers=headers, data = auctionItem)
    return response

# helper method to create object the way the back end likes
def createAuctionItemObject(title, description, endsIn):
    endtime = datetime.now() + timedelta(minutes=endsIn)
    endtime = endtime - timedelta(minutes=60) # Server timestamp is one hour behind ours
    myAuctionItem = {
        "title": title,
        "endDate": endtime.isoformat(),
        "price": 1,
        "description": description
    }
    return myAuctionItem