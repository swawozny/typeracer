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

    def getAvgWPM(request):
        return Game.objects.all().filter(user=request.user).aggregate(Avg('wpm'))['wpm__avg']

    def getAvgCPM(request):
        return Game.objects.all().filter(user=request.user).aggregate(Avg('cpm'))['cpm__avg']

    def getLastGame(request):
        return Game.objects.all().filter(user=request.user).order_by('-date')[0]

def save(self, *args, **kwargs):
    if self.score < 0:
        self.score = 0
    super(Game, self).save(*args, **kwargs)


def __unicode__(self):
    return unicode(self.date)
