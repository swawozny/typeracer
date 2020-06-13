from django.conf.urls import url
from django.urls import path

from .views import training_list, level_list

urlpatterns = [
    path('', training_list),
    url(r'^level-(?P<level_no>[\w-]+)/$', level_list),
]
