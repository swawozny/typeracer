from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    image = models.ImageField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/{}/".format(self.slug)

    def get_update_url(self):
        return "/news/{}/update/".format(self.slug)

    def get_delete_url(self):
        return "/news/{}/delete/".format(self.slug)

    def cut_text(self):
        return self.description[:670] + '...'


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    cellphone_num = models.IntegerField()

    def __str__(self):
        return self.user.username
