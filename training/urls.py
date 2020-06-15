from django.conf.urls import url
from django.urls import path

from .views import training_list, level_list, end_level_game

urlpatterns = [
    path('', training_list),
    url(r'^level-(?P<level_no>[\w-]+)/$', level_list),
    url(r'^level-(?P<level_no>[\w-]+)/end_level_game/$', end_level_game),
]
