"""typeracer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views, settings
from django.contrib.auth import views as auth_views
from register import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('ranking/', include('ranking.urls')),
    path('rejestracja/', include('register.urls')),
    path('profile/', user_views.profile, name='profile'),
    path('onas/', include('about.urls')),
    path('aktualnosci/', include('news.urls')),
    path('chatbox/', include('chatbox.urls')),
    path('typeracer/', include('typer.urls')),
    path('logowanie/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('wylogowanie/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
