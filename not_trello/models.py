from django.db import models


# Create your models here.
class Card(models.Model):
    activity = models.CharField(max_length=500)
    description = models.TextField()
    who_created = models.CharField(max_length=35)
    when_created = models.DateTimeField(auto_now_add=True)
    who_updated = models.CharField(max_length=35)
    when_updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    status = models.CharField(max_length=200)
    cards = models.ForeignKey(Card, on_delete=models.CASCADE)


class Board(models.Model):
    name = models.CharField(max_length=500)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
