from django.contrib.auth.models import User
from django.db import models
from register.models import Levels


class Achievements(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    Images = (
        ('/media/ranks/Beginner.png', 'Beginner'),
        ('/media/ranks/Intermediate.png', 'Intermediate'),
        ('/media/ranks/Average.png', 'Average'),
        ('/media/ranks/Pro.png', 'Pro'),
        ('/media/ranks/Typemaster.png', 'Typemaster'),
        ('/media/ranks/Megaracer.png', 'Megaracer'),
    )
    image = models.ImageField(
        choices=Images
    )

    rank = models.TextField(choices=Levels.choices(), default=Levels.Beginner)

    def __str__(self):
        return self.name

