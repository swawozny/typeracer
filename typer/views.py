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
            wpm=request.POST.get('wpm'),
            cpm=request.POST.get('cpm'),
            errors=request.POST.get('errors'),
        )
        models.update_user(request, request.POST.get('wpm'), request.POST.get('cpm'), request.POST.get('errors'))
        game.save()
        return JsonResponse({'status': True})
