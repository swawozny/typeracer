from register.models import Profile
from typer.models import Game


def statistics(request):
    if not request.user.is_authenticated:
        return {}
    else:
        if Game.objects.all().filter(user=request.user).exists():
            profile = Profile.objects.get(user=request.user)
            last_game = Game.objects.all().filter(user=request.user).order_by('-date')[0]
            return {'wpm': profile.avg_wpm, 'cpm': profile.avg_cpm, 'last_game': last_game}
        else:
            return {'wpm': 'None', 'cpm': 'None', 'last_game': []}
