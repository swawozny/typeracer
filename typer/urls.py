from django.conf.urls import url
from django.urls import path

from typer import views

urlpatterns = [
    path('', views.typer_list),
    url(r'^end_game/', views.end_game),
]
