from django import forms

from news.models import Post


class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
    slug = forms.CharField()


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'slug']