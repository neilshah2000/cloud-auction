from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user

class AuctionItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    endDate = models.DateTimeField()


class Bid(models.Model):
    amount = models.FloatField()
    time = models.DateTimeField()
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    created_by = models.ForeignKey('auth.User', default=get_current_user, on_delete=models.CASCADE)