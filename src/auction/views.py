from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import AuctionItem, Bid
from .serializers import AuctionItemSerializer, BidSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .tasks import createEndAuctionJob

# https://www.django-rest-framework.org/api-guide/viewsets/

class AuctionItemViewSet(viewsets.ModelViewSet):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer



from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    print(request.user)
    return HttpResponse(html)

def getBidsForItem(request, itemId):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    print(request.user)
    a = AuctionItem(id=itemId)
    # b = Bid(amount=500, time="2020-03-13T10:10:00Z", item=a)
    # b.save()
    all = Bid.objects.all()
    myItem = Bid(item=a)
    # bAll = bids.objects.all()

    some = Bid.objects.all().filter(item=a)

    serializer = BidSerializer(some, many=True)
    json = JSONRenderer().render(serializer.data)
    return HttpResponse(json)

@api_view(['POST'])
@login_required
def createBid(request):
    bid = BidSerializer(data=request.data)
    if bid.is_valid():
        bid.save()
        return Response(bid.data)
    return Response(bid.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@login_required
def createAuction(request):
    auctionItem = AuctionItemSerializer(data=request.data)
    if auctionItem.is_valid() and canBidOnItem(request):
        auctionInDB = auctionItem.save()
        createEndAuctionJob(auctionInDB.id, schedule=auctionInDB.endDate)
        return Response(auctionItem.data)
    return Response(auctionItem.errors, status=status.HTTP_400_BAD_REQUEST)

def endAuction():
    print('got to end the auction')

def canBidOnItem(request):
    # check if bid user is not the same as auction user
    # check if auction has not ended
    return True