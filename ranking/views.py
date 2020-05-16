from datetime import datetime
from datetime import timedelta

from django.contrib import messages
from django.shortcuts import render
from pytz import utc

from register.models import Profile
from typer.models import Game


# Create your views here.
def ranking_list(request):
    hours, days, weeks, months, years, forever = get_games()
    users_words, users_avg_cpm, users_race, users_avg_wpm = get_users_games()
    my_wpm, my_cpm, my_error, my_date = get_my_games(request)
    return render(request, 'ranking/ranking_list.html', {
        'hours': hours, 'days': days, 'weeks': weeks, 'months': months, 'years': years, 'forever': forever,
        'my_wpm': my_wpm, 'my_cpm': my_cpm, 'my_error': my_error, 'my_date': my_date,
        'users_words': users_words, 'users_avg_cpm': users_avg_cpm, 'users_race': users_race,
        'users_avg_wpm': users_avg_wpm
    })


def get_games():
    games1 = date_diff_in_minutes(Game.objects.all().filter(
        date__range=[datetime.now() - timedelta(hours=1), datetime.now()]).order_by('-wpm')[:20])
    games2 = date_diff_in_hours(Game.objects.all().filter(
        date__range=[datetime.now() - timedelta(days=1), datetime.now()]).order_by('-wpm')[:20])
    games3 = date_diff_in_days(Game.objects.all().filter(
        date__range=[datetime.now() - timedelta(days=7), datetime.now()]).order_by('-wpm')[:20])
    games4 = date_diff_in_days(Game.objects.all().filter(
        date__range=[datetime.now() - timedelta(days=30), datetime.now()]).order_by('-wpm')[:20])
    games5 = date_diff_in_days(Game.objects.all().filter(
        date__range=[datetime.now() - timedelta(days=365), datetime.now()]).order_by('-wpm')[:20])
    games6 = date_diff_in_days(Game.objects.all().order_by('-wpm')[:20])
    return games1, games2, games3, games4, games5, games6


def date_diff_in_minutes(games):
    for game in games:
        game.date = str((utc.localize(datetime.now()) - game.date).seconds // 60) + ' min ago'
    return games


def date_diff_in_hours(games):
    for game in games:
        time_seconds = (utc.localize(datetime.now()) - game.date).seconds
        game.date = str(time_seconds // 3600) + ' h ' + str((time_seconds // 60) % 60) + ' min ago'
    return games


def date_diff_in_days(games):
    for game in games:
        time_seconds = (utc.localize(datetime.now()) - game.date).seconds
        game.date = str(time_seconds // 86400) + ' d ' \
                    + str(time_seconds // 3600) + ' h ' \
                    + str((time_seconds // 60) % 60) + ' min ago'
    return games


def get_users_games():
    users_words = Profile.objects.all().order_by('-words')[:20]
    users_avg_cpm = Profile.objects.all().order_by('-avg_cpm')[:20]
    users_avg_wpm = Profile.objects.all().order_by('-avg_wpm')[:20]
    users_race = Profile.objects.all().order_by('-races')[:20]
    return users_words, users_avg_cpm, users_race, users_avg_wpm




def get_my_games(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Musisz zalogować się, żeby zobaczyć My Scores')
        return None, None, None, None
    wpm = Game.objects.all().filter(user=request.user).order_by('-wpm')[:20]
    cpm = Game.objects.all().filter(user=request.user).order_by('-cpm')[:20]
    error = Game.objects.all().filter(user=request.user).order_by('errors')[:20]
    date = Game.objects.all().filter(user=request.user).order_by('-date')[:20]
    return wpm, cpm, error, date
