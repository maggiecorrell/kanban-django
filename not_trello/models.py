from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=500)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Category(models.Model):
    board = models.ForeignKey(Board)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Card(models.Model):
    activity = models.CharField(max_length=500)
    category = models.ForeignKey(Category)
    # description = models.TextField()
    # status = models.CharField(max_length=200)
    # who_created = models.CharField(max_length=35)
    # when_created = models.DateTimeField(auto_now_add=True)
    # who_updated = models.CharField(max_length=35)
    # when_updated = models.DateTimeField(auto_now=True)
