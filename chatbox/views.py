from django.shortcuts import render

from django.shortcuts import render

def chatbox_list(request):
    return render(request, 'chatbox/chatbox_list.html')
