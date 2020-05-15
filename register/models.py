from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models import Avg

from typer.models import Game


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    words = models.IntegerField(null=False, default=0)
    characters = models.IntegerField(null=False, default=0)
    avg_cpm = models.IntegerField(null=False, default=0)
    avg_wpm = models.IntegerField(null=True)
    avg_accuracy = models.FloatField(null=True)
    races = models.IntegerField(null=False, default=0)
    errors = models.IntegerField(null=False, default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

def update_user(request, wpm, cpm, errors):
    profile = Profile.objects.filter(user=request.user)
    new_words = profile.words + int(wpm)
    new_characters = profile.characters + int(cpm)
    new_errors = profile.errors + int(errors)
    new_races = profile.races + 1
    new_cpm = new_characters/new_races
    new_wpm = new_words/new_races
    new_avg_accuracy = new_errors/new_characters

    Profile.objects.select_related().update(words = new_words, characters = new_characters, errors = new_errors,
                                            races = new_races, avg_cpm = new_cpm, avg_wpm = new_wpm,
                                            avg_accuracy = new_avg_accuracy)



