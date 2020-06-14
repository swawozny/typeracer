from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from register import models
from register.models import Profile
from training.models import Level, LevelResult


def training_list(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Log in to train your typing skills')
        user_training_lvl = None
    else:
        user_training_lvl = get_user_training_lvl(request)
    levels = Level.objects.all().order_by('level_no')
    context = {
        'levels': levels,
        'user_training_lvl': user_training_lvl
    }
    return render(request, 'training/training.html', context)


def level_list(request, level_no):
    if not request.user.is_authenticated:
        return redirect('/login/?next=' + request.path)
    elif get_user_training_lvl(request) < int(level_no):
        return redirect('/')
    else:
        unique_level = get_object_or_404(Level, level_no=level_no)
        return render(request, 'training/level.html', {'level': unique_level})


def get_user_training_lvl(request):
    return Profile.objects.get(user=request.user).training_lvl.level_no


@login_required()
def end_level_game(request, level_no):
    if request.method == 'POST':
        wpm = request.POST.get('wpm')
        min_wpm = Level.objects.get(level_no=level_no).min_wpm
        errors = request.POST.get('errors')
        max_errors = Level.objects.get(level_no=level_no).max_err
        if int(wpm) >= min_wpm and int(errors) <= max_errors:
            level = Level.objects.get(level_no=level_no)
            if LevelResult.objects.filter(level=level, user=request.user).count() == 0:
                level_result = LevelResult.objects.create(
                    user=request.user,
                    level=get_object_or_404(Level, level_no=level_no),
                    wpm=get_wpm(request),
                    cpm=get_cpm(request),
                    errors=get_errors(request),
                )
                models.update_user(request, get_wpm(request), get_cpm(request), get_errors(request), level_no)
            else:
                level_result = LevelResult.objects.get(level=level_no)
                level_result.wpm = get_wpm(request)
                level_result.cpm = get_cpm(request)
                level_result.errors = get_errors(request)
            level_result.save()
        return JsonResponse({'status': True})


def get_wpm(request):
    return request.POST.get('wpm')


def get_cpm(request):
    return request.POST.get('cpm')


def get_errors(request):
    return request.POST.get('errors')
