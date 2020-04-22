from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostModelForm
from django.shortcuts import render
from django.contrib import messages

from news.models import Post, Author


def news_list(request):
    all_posts = Post.objects.all().order_by('date')
    context = {
        'all_posts': all_posts
    }
    messages.info(request, 'Tutaj są wszystkie aktualności')
    return render(request, 'news/news_list.html', context)


# CRUD
# CREATE RETRIEVE UPDATE AND DELETE
def news_detail(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {
        'post': unique_post
    }
    messages.info(request, 'Tutaj jest rozwinięcie wpisu')
    return render(request, "news/news_detail.html", context)


def posts_create(request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        email=request.user.email,
        cellphone_num=894382982)
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        messages.info(request, 'Udało się dodać wpis')
        return redirect('/aktualnosci/')
    context = {
        'form': form
    }
    return render(request, "news/news_create.html", context)


def posts_update(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None,
                         request.FILES or None,
                         instance=unique_post)
    if form.is_valid():
        form.save()
        messages.info(request, 'Udało się zaktualizować post')
        return redirect('/aktualnosci/')
    context = {
        'form': form
    }
    return render(request, "news/posts_update.html", context)


def posts_delete(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    messages.info(request, 'Udało się usunąć wpis')
    return redirect('/aktualnosci/')
