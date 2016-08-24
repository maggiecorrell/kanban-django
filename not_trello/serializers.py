from rest_framework import serializers
from .models import Board, Category, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('activity', 'description', 'status')
        # 'who_created', 'when_created', 'who_editied', 'when_edited'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('cards')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'categories')
