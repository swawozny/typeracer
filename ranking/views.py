from django.shortcuts import render
from .models import Osoba

# Create your views here.
def ranking_list(request):
    ranking = Osoba.objects.all().order_by('date')
    return render(request, 'ranking/ranking_list.html', {'ranking': ranking})
