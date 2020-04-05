from background_task import background
from django.contrib.auth.models import User
from django.db.models import Max
from datetime import datetime
from .models import AuctionItem, Bid
from .serializers import AuctionItemSerializer, BidSerializer

@background(schedule=1)
def createEndAuctionJob(auctionItemId):
    auction = AuctionItem.objects.get(pk=auctionItemId)
    bestBid = findWinningBid(auctionItemId)
    auction.ended = True
    auction.winner = bestBid
    auction.save()
    print('Auction ended: ', AuctionItemSerializer(auction).data)
    print(datetime.now())

def findWinningBid(auctionItemId):
    allBids = Bid.objects.all().filter(item_id=auctionItemId)
    bestBid = allBids.order_by('amount').last()
    if bestBid is not None:
        print('Best bid: ', BidSerializer(bestBid).data)
    else:
        print('no bids')
    return bestBid