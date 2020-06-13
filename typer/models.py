from datetime import datetime

from django.db import models
from django.db.models import Avg
from numpy import unicode

from news.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wpm = models.IntegerField(default=0, null=True)
    cpm = models.IntegerField(default=0, null=True)
    errors = models.IntegerField(default=0, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def get_avg_wpm(self):
        return Game.objects.all().filter(user=self.user).aggregate(Avg('wpm'))['wpm__avg']

    def get_avg_cpm(self):
        return Game.objects.all().filter(user=self.user).aggregate(Avg('cpm'))['cpm__avg']

    def get_last_name(self):
        return Game.objects.all().filter(user=self.user).order_by('-date')[0]


def save(self, *args, **kwargs):
    if self.score < 0:
        self.score = 0
    super(Game, self).save(*args, **kwargs)


def __unicode__(self):
    return unicode(self.date)
