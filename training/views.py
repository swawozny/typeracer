from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from register.models import Profile
from training.models import Level


def training_list(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Log in to train your typing skills')
        user_training_lvl = None
    else:
        user_training_lvl = Profile.objects.get(user=request.user).training_lvl.level_no
    levels = Level.objects.all().order_by('level_no')
    return render(request, 'training/training.html', {'levels': levels, 'user_training_lvl': user_training_lvl})


def level_list(request, level_no):
    unique_level = get_object_or_404(Level, level_no=level_no)
    return render(request, 'training/level.html', {'level': unique_level})
