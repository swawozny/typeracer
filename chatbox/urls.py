from django.conf.urls import url
from django.urls import path, include
from . import views
from chatbox.views import JoinFormView

urlpatterns = [

    url('', JoinFormView.as_view()),

]

