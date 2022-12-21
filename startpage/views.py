from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return HttpResponse('Страница')
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')