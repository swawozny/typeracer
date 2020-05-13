from django.shortcuts import render
from django.contrib import messages


def home(request):
    messages.info(request, 'Tutaj możesz zagrać w grę OFFLINE')
    return render(request, 'home.html')
