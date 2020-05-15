import json
from datetime import datetime

import simplejson as simplejson
from django.contrib.auth.decorators import login_required
from django.contrib.postgres import serializers
from django.http import JsonResponse, HttpResponse, request, response
from django.shortcuts import render
from django.contrib import messages

from .forms import MessageForm
from .models import Game
from django.views.decorators.http import require_POST
from register import models

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
        models.update_user(request, request.POST.get('wpm'), request.POST.get('cpm'), request.POST.get('errors'))
        game.save()
        return JsonResponse({'status': True})
