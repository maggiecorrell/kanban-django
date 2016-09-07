from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Card(models.Model):
    activity = models.CharField(max_length=500)
    # description = models.TextField()
    # status = models.CharField(max_length=200)
    # who_created = models.CharField(max_length=35)
    # when_created = models.DateTimeField(auto_now_add=True)
    # who_updated = models.CharField(max_length=35)
    # when_updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    cards = models.ForeignKey(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Board(models.Model):
    name = models.CharField(max_length=500)
    user = models.ManyToManyField(User)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
