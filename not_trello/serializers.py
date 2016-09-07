from rest_framework import serializers
from .models import Board, Category, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'activity',)
        # 'status', 'who_created', 'when_created', 'who_editied', 'when_edited'


class CategorySerializer(serializers.ModelSerializer):
    cards_set = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'cards_set', 'name')


class BoardSerializer(serializers.ModelSerializer):
    categories_set = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'user', 'categories_set')
