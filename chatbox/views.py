import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from news.models import Post
from django.views.generic import FormView

from .forms import JoinForm
from .mixins import AjaxFormMixin


def chatbox_list(request):
    return render(request, 'chatbox/chatbox_list.html')


class JoinFormView(FormView):
    form_class = JoinForm
    template_name = 'chatbox/chatbox_list.html'
    success_url = '/form-success/'

    def form_invalid(self, form):
        response = super(JoinFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response