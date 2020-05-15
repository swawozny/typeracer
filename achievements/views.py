from django.shortcuts import render


# Create your views here.
def achievements_list(request):
    return render(request, 'achievements/achievements_list.html')
