from django.shortcuts import render
from .serializers import BoardSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.views import generic
from .models import Board, Card, Category
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views import View
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'index.html')


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all().order_by('name')
