from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from register import models
from .models import Game


def typer_list(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Log in to remember your stats and observe your progress')
    return render(request, 'typer/typer.html')


@login_required()
def end_game(request):
    if request.method == 'POST':
        game = Game.objects.create(
            user=request.user,
            wpm=get_wpm(request),
            cpm=get_cpm(request),
            errors=get_errors(request),
        )
        models.update_user(request, get_wpm(request), get_cpm(request), get_errors(request), None)
        game.save()
        return JsonResponse({'status': True})


def get_wpm(request):
    return request.POST.get('wpm')


def get_cpm(request):
    return request.POST.get('cpm')


def get_errors(request):
    return request.POST.get('errors')
