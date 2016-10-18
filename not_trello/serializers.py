from rest_framework import serializers
from .models import Board, Category, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'activity',)
        # 'status', 'who_created', 'when_created', 'who_editied', 'when_edited'


class CategorySerializer(serializers.ModelSerializer):
<<<<<<< HEAD

    class Meta:
        model = Category
        fields = ('id', 'name')
=======
    cards_set = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'cards_set', 'name')
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603


class BoardSerializer(serializers.ModelSerializer):
    categories_set = CategorySerializer(many=True, read_only=True)
<<<<<<< HEAD
    cards_set = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'user', 'categories_set', 'cards_set')
=======

    class Meta:
        model = Board
        fields = ('id', 'name', 'user', 'categories_set')
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603
