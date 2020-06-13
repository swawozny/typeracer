from django.db import models


class Level(models.Model):
    level_no = models.IntegerField(null=False, unique=True)
    max_err = models.IntegerField(null=False)
    min_wpm = models.IntegerField(null=False)
    text = models.TextField(null=False)

    def __str__(self):
        return f'Level {self.level_no}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return "/level-{}/".format(self.level_no)
