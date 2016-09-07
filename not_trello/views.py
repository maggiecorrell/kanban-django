from django.shortcuts import render
from .serializers import BoardSerializer, CategorySerializer, CardSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Board, Card, Category


# @login_required
def index(request):
    return render(request, 'index.html')


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all().order_by('name')


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


def board(request):
    pass
