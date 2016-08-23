from django.shortcuts import render, HttpResponse


def index(self):
    return HttpResponse('Hello World')
