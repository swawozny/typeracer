from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def ranking(request):
    return render(request, 'ranking.html')


def typeracer(request):
    return render(request, 'typeracer.html')


def rejestracja(request):
    return render(request, 'typeracer.html')
