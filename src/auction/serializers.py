from rest_framework import serializers
from .models import AuctionItem
from .models import Bid

class AuctionItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuctionItem
        fields = ('title', 'description', 'price', 'endDate')


class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ('amount', 'time', 'item')