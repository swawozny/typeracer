from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

ACHIEVEMENT_FIRST_LVL = 1
ACHIEVEMENT_SECOND_LVL = 2
ACHIEVEMENT_THIRD_LVL = 3
ACHIEVEMENT_FOURTH_LVL = 4
ACHIEVEMENT_FIFTH_LVL = 5
ACHIEVEMENT_SIXTH_LVL = 6

ACHIEVEMENT_CHOICES = (
    (ACHIEVEMENT_FIRST_LVL, _('Beginner')),
    (ACHIEVEMENT_SECOND_LVL, _('Intermediate')),
    (ACHIEVEMENT_THIRD_LVL, _('Average')),
    (ACHIEVEMENT_FOURTH_LVL, _('Pro')),
    (ACHIEVEMENT_FIFTH_LVL, _('Typemaster')),
    (ACHIEVEMENT_SIXTH_LVL, _('Megaracer')),
)


class Achievements(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    typing_lvl = models.PositiveSmallIntegerField(choices=ACHIEVEMENT_CHOICES, default=ACHIEVEMENT_FIRST_LVL)
    score_lvl = models.PositiveSmallIntegerField(choices=ACHIEVEMENT_CHOICES, default=ACHIEVEMENT_FIRST_LVL)
    races_lvl = models.PositiveSmallIntegerField(choices=ACHIEVEMENT_CHOICES, default=ACHIEVEMENT_FIRST_LVL)
    accuracy_lvl = models.PositiveSmallIntegerField(choices=ACHIEVEMENT_CHOICES, default=ACHIEVEMENT_FIRST_LVL)
    progress_lvl = models.PositiveSmallIntegerField(choices=ACHIEVEMENT_CHOICES, default=ACHIEVEMENT_FIRST_LVL)

    def __str__(self):
        return f'{self.user.username} Achievements'
