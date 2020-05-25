import enum

from django.contrib.auth.models import User
from django.db import models

from typer.models import Game


class Levels(enum.Enum):
    Beginner = 1
    Intermediate = 2
    Average = 3
    Pro = 4
    Typemaster = 5
    Megaracer = 6


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

    def get_typing_lvl(self):
        if self.avg_wpm < 25:
            return Levels.Beginner.name
        elif self.avg_wpm < 31:
            return Levels.Intermediate.name
        elif self.avg_wpm < 42:
            return Levels.Average.name
        elif self.avg_wpm < 55:
            return Levels.Pro.name
        elif self.avg_wpm < 80:
            return Levels.Typemaster.name
        else:
            return Levels.Megaracer.name

    def get_score_lvl(self):
        if self.words < 100:
            return Levels.Beginner.name
        elif self.words < 500:
            return Levels.Intermediate.name
        elif self.words < 2500:
            return Levels.Average.name
        elif self.words < 10000:
            return Levels.Pro.name
        elif self.words < 50000:
            return Levels.Typemaster.name
        else:
            return Levels.Megaracer.name

    def get_races_lvl(self):
        if self.races < 10:
            return Levels.Beginner.name
        elif self.races < 30:
            return Levels.Intermediate.name
        elif self.races < 60:
            return Levels.Average.name
        elif self.races < 100:
            return Levels.Pro.name
        elif self.races < 300:
            return Levels.Typemaster.name
        else:
            return Levels.Megaracer.name

    def get_accuracy_lvl(self):
        if self.avg_accuracy < 3:
            return Levels.Megaracer.name
        elif self.avg_accuracy < 5:
            return Levels.Typemaster.name
        elif self.avg_accuracy < 10:
            return Levels.Pro.name
        elif self.avg_accuracy < 20:
            return Levels.Average.name
        elif self.avg_accuracy < 30:
            return Levels.Intermediate.name
        else:
            return Levels.Beginner.name

    def get_summary_lvl(self):

        ranks = [self.get_accuracy_lvl(), self.get_races_lvl(), self.get_score_lvl(), self.get_typing_lvl()]

        points = 0

        for rank in ranks:
            if rank == Levels.Beginner.name:
                points += 10
            elif rank == Levels.Intermediate.name:
                points += 20
            elif rank == Levels.Average.name:
                points += 30
            elif rank == Levels.Pro.name:
                points += 40
            elif rank == Levels.Typemaster.name:
                points += 50
            else:
                points += 60

        if points < 60:
            return Levels.Beginner.name
        elif points < 120:
            return Levels.Intermediate.name
        elif points < 180:
            return Levels.Average.name
        elif points < 240:
            return Levels.Pro.name
        elif points < 300:
            return Levels.Typemaster.name
        elif points >= 300:
            return Levels.Megaracer.name


def update_user(request, wpm, cpm, errors):
    try:
        profile = Profile.objects.get(user=request.user)
        profile.words += int(wpm)
        profile.characters += int(cpm)
        profile.errors += int(errors)
        profile.races += 1
        profile.avg_cpm = (profile.characters) / profile.races
        profile.avg_wpm = (profile.words) / profile.races
        if profile.characters + int(cpm) != 0:
            profile.avg_accuracy = 1 - ((profile.errors) / profile.characters)
        else:
            new_avg_accuracy = None

        profile.save()
    except:
        console.log("Cannot save profile")
