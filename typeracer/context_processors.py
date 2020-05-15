from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from register.models import Profile
from typer.models import Game

def statisitcs(request):
    if not request.user.is_authenticated:
        return{}
    else:
        if Game.objects.all().filter(user=request.user).exists():
            profile = Profile.objects.get(user=request.user)
            lastgame = Game.objects.all().filter(user=request.user).order_by('-date')[0]
            return {'wpm': profile.avg_wpm, 'cpm': profile.avg_cpm, 'lastgame': lastgame}
        else:
            return {'wpm': 'BRAK', 'cpm': 'BRAK', 'lastgame': []}
