<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603
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

<<<<<<< HEAD
    # def get_queryset(self):
    #     user =self.request.user
    #     queryset = Board.objects.all()
    #     return queryset


=======
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

<<<<<<< HEAD
# wells = Well.objects.all()
#     well = get_object_or_404(Well, id=well_id)
#     total_use = HourlyUsage.objects.filter(
#                             well_id=well.id).aggregate(sum=Sum('usage_count'))

def board_detail(request, board_id):
    boards = get_object_or_404(Board, id=board_id)
    # user = request.user
    # boards = Board.objects.filter(user=user)

    # if request.POST:
    #     category_name = request.POST.get('category_name', '')
    #     if category_name:
    #         category = Category(name=category_name, boards=boards)
    #         category.save()

    # categories = Board.objects.get(boards)
    context = {
        'boards': boards,
        # 'categories': categories,
    }
    return render(request, 'board_detail.html', context)
=======

def board(request):
    pass
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603
