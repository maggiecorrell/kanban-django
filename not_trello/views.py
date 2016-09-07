from django.shortcuts import render
from .serializers import BoardSerializer, CategorySerializer, CardSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Board, Card, Category


@login_required
def index(request):
    user = request.user

    if request.POST:
        board_name = request.POST.get('board-name', '')
        board = Board(name=board_name)
        board.save()
        board.user.add(user)
        board.save()

    boards = Board.objects.filter(user=user)
    context = {
        'boards': boards
    }

    return render(request, 'index.html', context)


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


def board(request):
    pass
