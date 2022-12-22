

from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseNotFound


# Create your views here.
from startpage.models import Account


def index(request):
    return render(request, 'index.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def register(request):
    try:
        email = str(request.GET.get('email'))
        password = str(request.GET.get('pass'))
        Account.objects.create(email=email, password=password)
    except:
        return HttpResponse('<h1>Error</h1>')