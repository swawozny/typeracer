from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from typer.models import Game


def statisitcs(request):
    if not request.user.is_authenticated:
        return{}
    else:
        if Game.objects.all().filter(user=request.user).exists():
            avgwpm = Game.objects.all().filter(user=request.user).aggregate(Avg('wpm'))['wpm__avg']
            avgcpm = Game.objects.all().filter(user=request.user).aggregate(Avg('cpm'))['cpm__avg']
            lastgame = Game.objects.all().filter(user=request.user).order_by('-date')[0]
            return {'wpm': avgwpm, 'cpm': avgcpm, 'lastgame': lastgame}
        else:
            return {'wpm': 'BRAK', 'cpm': 'BRAK', 'lastgame': []}
