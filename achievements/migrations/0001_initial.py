# Generated by Django 3.0.5 on 2020-05-15 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typing_lvl', models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Average'), (4, 'Pro'), (5, 'Typemaster'), (6, 'Megaracer')], default=1)),
                ('score_lvl', models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Average'), (4, 'Pro'), (5, 'Typemaster'), (6, 'Megaracer')], default=1)),
                ('races_lvl', models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Average'), (4, 'Pro'), (5, 'Typemaster'), (6, 'Megaracer')], default=1)),
                ('accuracy_lvl', models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Average'), (4, 'Pro'), (5, 'Typemaster'), (6, 'Megaracer')], default=1)),
                ('progress_lvl', models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Average'), (4, 'Pro'), (5, 'Typemaster'), (6, 'Megaracer')], default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
