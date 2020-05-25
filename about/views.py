from django.shortcuts import render

def about_list(request):
    return render(request, 'about/about.html')
