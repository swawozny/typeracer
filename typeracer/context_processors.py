from django.db.models import Avg

from typer.models import Game


def statisitcs(request):
    if not request.user.is_authenticated:
        return {}
    else:
        if Game.objects.all().filter(user=request.user).exists():
            avgwpm = Game.objects.all().filter(user=request.user).aggregate(Avg('wpm'))['wpmavg']
            avgcpm = Game.objects.all().filter(user=request.user).aggregate(Avg('cpm'))['cpmavg']
            lastgame = Game.objects.all().filter(user=request.user).order_by('-date')[0]
            return {'wpm': avgwpm, 'cpm': avgcpm, 'lastgame': lastgame}
        else:
            return {'wpm': 'BRAK', 'cpm': 'BRAK', 'lastgame': []}
