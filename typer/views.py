from django.shortcuts import render

from django.shortcuts import render

def typer_list(request):
    return render(request, 'typer/typer_list.html')
