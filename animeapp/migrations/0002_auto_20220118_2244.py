# Generated by Django 3.2.9 on 2022-01-18 13:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Animes',
            new_name='Anime',
        ),
        migrations.RenameModel(
            old_name='favorites',
            new_name='favorite',
        ),
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='Rationgs',
            new_name='Rationg',
        ),
    ]