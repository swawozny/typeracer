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

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from register import views as user_views
from typeracer import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('training.urls')),
    path('ranking/', include('ranking.urls')),
    path('achievements/', include('achievements.urls')),
    path('register/', include('register.urls')),
    path('profile/', user_views.profile, name='profile'),
    path('about/', include('about.urls')),
    path('news/', include('news.urls')),
    path('typeracer/', include('typer.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', user_views.logout_list, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
