# Generated by Django 3.0.6 on 2020-05-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_remove_profile_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avg_cpm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='characters',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='errors',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='races',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='words',
            field=models.IntegerField(default=0),
        ),
    ]
