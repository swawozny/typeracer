from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from register.models import Profile
from training.models import Level


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
