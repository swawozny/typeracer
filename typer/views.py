from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Game


def typer_list(request):
    messages.info(request, 'Tutaj możesz zagrać w grę ONLINE')
    return render(request, 'typer/typer_list.html')


@login_required()
def end_game(request):
    if request.method == 'POST':
        game = Game.objects.create(
            user=request.user,
            wpm=request.POST.get('wpm'),
            cpm=request.POST.get('cpm'),
            errors=request.POST.get('errors'),
        )
        game.save()
        return JsonResponse({'status': True})
