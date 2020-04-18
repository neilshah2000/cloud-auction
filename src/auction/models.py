from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user
from datetime import datetime, timezone

class AuctionItem(models.Model):

    # https://docs.djangoproject.com/en/dev/ref/models/fields/#field-choices-enum-types
    class Condition(models.TextChoices):
        NEW = 'New'
        USED = 'Used'
    

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=Condition.choices, default=Condition.USED)
    price = models.FloatField()
    endDate = models.DateTimeField()
    ended = models.BooleanField(default=False)
    winner = models.ForeignKey('Bid', on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey('auth.User', default=get_current_user, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def timeLeft(self):
        if self.ended: return 'Auction ended'
        else:
            left = self.endDate - datetime.now(timezone.utc)
            return str(left)

class Bid(models.Model):
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    created_by = models.ForeignKey('auth.User', default=get_current_user, on_delete=models.CASCADE)