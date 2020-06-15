from django.contrib import messages
from django.shortcuts import render

from register.models import Profile
from .models import Achievements


def achievements_list(request):
    typing_lvl = None
    score_lvl = None
    races_lvl = None
    accuracy_lvl = None
    summary_lvl = None

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        typing_lvl = profile.get_typing_lvl()
        score_lvl = profile.get_score_lvl()
        races_lvl = profile.get_races_lvl()
        accuracy_lvl = profile.get_accuracy_lvl()
        summary_lvl = profile.get_summary_lvl()
        achievements = Achievements.objects.all()
    else:
        messages.info(request, 'You must be logged to see your Achievements')

    return render(request, 'achievements/achievements.html', {
        'typing_lvl': typing_lvl,
        'score_lvl': score_lvl,
        'races_lvl': races_lvl,
        'accuracy_lvl': accuracy_lvl,
        'summary_lvl': summary_lvl,
        'achievements': achievements,
    })
