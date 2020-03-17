from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import AuctionItem, Bid
from .serializers import AuctionItemSerializer, BidSerializer

# https://www.django-rest-framework.org/api-guide/viewsets/

class AuctionItemViewSet(viewsets.ModelViewSet):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    # @action(detail=True, methods=['post'])
    # def bidOnItem(self, request, pk=None):
    #     print(request.user)



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
    bids = Bid(item=a)

    serializer = BidSerializer(all, many=True)
    json = JSONRenderer().render(serializer.data)
    return HttpResponse(json)