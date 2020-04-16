import requests
import json
from login import loginUser
from addItem import addAuctionItem
from datetime import datetime, timedelta

mary = {'username': 'mary', 'password': 'mary'}
maryToken = loginUser(mary)

minutesToEnd = 10
response = addAuctionItem('Marys Item', 'mary adds an item', minutesToEnd, maryToken)

print(response.json())
    
