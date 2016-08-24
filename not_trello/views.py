from django.shortcuts import render
from .serializers import BoardSerializer
from rest_framework import viewsets
# from django.http import HttpResponse
from .models import Board, Card, Category


def index(request):
    return render(request, 'board.html')


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all().order_by('name')
