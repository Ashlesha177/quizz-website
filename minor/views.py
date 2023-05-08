from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def joinus(request):
    return render(request, 'joinus.html')


def categories(request):
    return render(request, 'categories.html')

# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("charcount  <a href='/'>back</a>")
