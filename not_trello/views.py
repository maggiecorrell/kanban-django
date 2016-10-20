from django.shortcuts import render, get_object_or_404
from .serializers import BoardSerializer, CategorySerializer, CardSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Board, Card, Category


@login_required
def index(request):
    user = request.user

    if request.POST:
        board_title = request.POST.get('board-title', '')
        board = Board(title=board_title)
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

    # def get_queryset(self):
    #     user =self.request.user
    #     queryset = Board.objects.all()
    #     return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


# wells = Well.objects.all()
#     well = get_object_or_404(Well, id=well_id)
#     total_use = HourlyUsage.objects.filter(
#                             well_id=well.id).aggregate(sum=Sum('usage_count'))

def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.POST:
        category_name = request.POST.get('category-name', '')
        category = Category(name=category_name, board_id=board_id)
        category.save()

    try:
        categories = board.category_set.all()
    except:
        categories = None

    context = {
        'board': board,
        'categories': categories,
    }
    return render(request, 'board_detail.html', context)
