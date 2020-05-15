from django.db import models


class Osoba(models.Model):
    name = models.CharField(max_length=30)
    body = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
