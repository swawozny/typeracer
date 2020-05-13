from django.contrib import messages
from django.shortcuts import render
from datetime import datetime
from datetime import timedelta

from typer.models import Game


# Create your views here.
def ranking(request):
    games = Game.objects.all().filter(
        date__range=[datetime.now() - timedelta(hours=1), datetime.now()]).order_by('-wpm')[:20]
    my_games = None
    if request.user.is_authenticated:
        my_games = Game.objects.all().filter(user=request.user).order_by('-wpm')[:20]
    else:
        messages.info(request, 'Musisz zalogować się, żeby zobaczyć My Scores')
    return render(request, 'ranking/ranking.html', {'games': games, 'my_games': my_games})

