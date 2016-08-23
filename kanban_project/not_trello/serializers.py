from rest_framework import serializers
from .models import Board, Catagory, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('activity', 'description', 'who_created', 'when_created', 'who_editied', 'when_edited')


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ('status', 'cards')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'categories')
