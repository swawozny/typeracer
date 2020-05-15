from django.db.models import Avg
from django.shortcuts import render
from django.contrib import messages

from typer import models
from typer.models import Game


def home(request):
    messages.info(request, 'Tutaj możesz zagrać w grę OFFLINE')
    return render(request, 'home.html')



