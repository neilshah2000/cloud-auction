from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import AuctionItem, Bid
from .serializers import AuctionItemSerializer, BidSerializer

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

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

class BidCreate(LoginRequiredMixin, CreateView):
    model = Bid
    fields = ['amount', 'item']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


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