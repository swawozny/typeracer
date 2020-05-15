from django.contrib.auth.models import User
from django.db import models

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
   try:
        profile = Profile.objects.get(user=request.user)
        profile.words += int(wpm)
        profile.characters += int(cpm)
        profile.errors += int(errors)
        profile.races += 1
        profile.avg_cpm = (profile.characters ) / profile.races
        profile.avg_wpm = (profile.words ) / profile.races
        if profile.characters + int(cpm) != 0:
            profile.avg_accuracy = 1 - ((profile.errors) / profile.characters)
        else:
            new_avg_accuracy = None

        profile.save()
   except:
        console.log("Cannot save profile")


