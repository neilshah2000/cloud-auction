from django.shortcuts import render

from rest_framework import viewsets
from .models import AuctionItem, Bid
from .serializers import AuctionItemSerializer, BidSerializer

class AuctionItemViewSet(viewsets.ModelViewSet):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer