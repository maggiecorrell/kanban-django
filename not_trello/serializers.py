from rest_framework import serializers
from .models import Board, Category, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'board', 'activity',)
        # 'status', 'who_created', 'when_created', 'who_editied', 'when_edited'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'board', 'name')


class BoardSerializer(serializers.ModelSerializer):
    categories_set = CategorySerializer(many=True, read_only=True)
    cards_set = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'user', 'categories_set', 'cards_set')
