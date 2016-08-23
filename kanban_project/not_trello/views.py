from django.shortcuts import render
from .models import Board
from .serializers import BoardSerializer
from rest_framework import viewsets


def index(request):
    return render(request, 'index.html')


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all().order_by('name')
