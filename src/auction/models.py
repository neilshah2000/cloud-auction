from django.db import models

class AuctionItem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    endDate = models.DateTimeField()


class Bid(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.FloatField()
    time = models.DateTimeField()
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)