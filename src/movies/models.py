from django.db import models
class Movies(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    score = models.FloatField()