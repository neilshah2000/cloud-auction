from background_task import background
from django.contrib.auth.models import User
from datetime import datetime
from .models import AuctionItem
from .serializers import AuctionItemSerializer

@background(schedule=1)
def createEndAuctionJob(auctionItemId):
    auction = AuctionItem.objects.get(pk=auctionItemId)
    print('Auction ended: ', AuctionItemSerializer(auction).data)
    print(datetime.now())