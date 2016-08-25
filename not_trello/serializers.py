from rest_framework import serializers
from .models import Board, Category, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'activity',)
        # 'status', 'who_created', 'when_created', 'who_editied', 'when_edited'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'cards',)


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'user', 'categories')
