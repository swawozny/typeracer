from datetime import datetime

from django.db import models

from news.models import User


class Level(models.Model):
    level_no = models.IntegerField(null=False, unique=True)
    max_err = models.IntegerField(null=False)
    min_wpm = models.IntegerField(null=False)
    time = models.IntegerField(null=False, default=60)
    text = models.TextField(null=False)

    def __str__(self):
        return f'Level {self.level_no}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return "/level-{}/".format(self.level_no)


class LevelResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.OneToOneField(Level, on_delete=models.CASCADE)
    wpm = models.IntegerField(default=0, null=True)
    cpm = models.IntegerField(default=0, null=True)
    errors = models.IntegerField(default=0, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'Level {self.level.level_no} result'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
