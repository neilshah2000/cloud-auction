from django.shortcuts import render
import json
from datetime import datetime
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import AuctionItem, Bid
from .serializers import AuctionItemSerializer, BidSerializer
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .tasks import createEndAuctionJob
from django.http import HttpResponse

# https://www.django-rest-framework.org/api-guide/viewsets/

class AuctionItemViewSet(viewsets.ModelViewSet):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer

    def create(self, request):
        auctionItem = AuctionItemSerializer(data=request.data)
        if auctionItem.is_valid():
            auctionInDB = auctionItem.save()
            createEndAuctionJob(auctionInDB.id, schedule=auctionInDB.endDate)
            return Response(auctionItem.data)
        return Response(auctionItem.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False)
    def available(self, request):
        sold = AuctionItem.objects.all().filter(ended=False)
        serializer = AuctionItemSerializer(sold, many=True)
        mJson = JSONRenderer().render(serializer.data)
        return HttpResponse(mJson)
    
    @action(detail=False)
    def sold(self, request):
        sold = AuctionItem.objects.all().filter(ended=True)
        serializer = AuctionItemSerializer(sold, many=True)
        mJson = JSONRenderer().render(serializer.data)
        return HttpResponse(mJson)
    
    @action(detail=True)
    def bids(self, request, pk):
        a = AuctionItem(id=pk)
        hist = Bid.objects.all().filter(item=a)
        serializer = BidSerializer(hist, many=True)
        mJson = JSONRenderer().render(serializer.data)
        if canViewBids(request, pk):
            return HttpResponse(mJson)
        else:
            return Response({'detail': 'Can not view this item'}, status=status.HTTP_400_BAD_REQUEST)



class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def create(self, request):
        bid = BidSerializer(data=request.data)
        if bid.is_valid():
            if canBidOnItem(request):
                if auctionNotFinished(request):
                    bid.save()
                    return Response(bid.data)
                else: return Response({'detail': 'The auction has ended'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'User can not bid on thier own auction'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(bid.errors, status=status.HTTP_400_BAD_REQUEST)




################ helpers ####################


# check if bid user is not the same as auction user
def canBidOnItem(request):
    bid = BidSerializer(data=request.data)
    if bid.is_valid():
        auctionItemId = bid.data['item']
        bidAuction = AuctionItem.objects.get(pk=auctionItemId)
        auctionUser = bidAuction.created_by_id
        bidUser = request.user.id
        return auctionUser != bidUser
    return False

# check if auction has not ended
def auctionNotFinished(request):
    bid = BidSerializer(data=request.data)
    if bid.is_valid():
        auctionItemId = bid.data['item']
        bidAuction = AuctionItem.objects.get(pk=auctionItemId)
        endDate = bidAuction.endDate
        now = timezone.now()
        return endDate > now
    return False

# check the user is viewing bids only on their own item
def canViewBids(request, auctionItemId):
    try:
        ai = AuctionItem.objects.get(pk=auctionItemId)
        return ai.created_by_id == request.user.id
    except AuctionItem.DoesNotExist:
        return False
