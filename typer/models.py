from datetime import datetime

from django.db import models
from numpy import unicode

from news.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wpm = models.IntegerField(default=0, null=True)
    cpm = models.IntegerField(default=0, null=True)
    errors = models.IntegerField(default=0, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)


def save(self, *args, **kwargs):
    if self.score < 0:
        self.score = 0
    super(Game, self).save(*args, **kwargs)


def __unicode__(self):
    return unicode(self.date)
