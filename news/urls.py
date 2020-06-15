from django.conf.urls import url
from django.urls import path

from .views import posts_create, news_detail, news_list, posts_update, posts_delete

urlpatterns = [
    path('', news_list),
    url(r'^create/$', posts_create),
    url(r'^(?P<slug>[\w-]+)/update/$', posts_update),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete),
    url(r'^(?P<slug>[\w-]+)/$', news_detail),
]
