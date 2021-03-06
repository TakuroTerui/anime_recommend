# Generated by Django 3.2.9 on 2022-01-22 14:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animeapp', '0003_auto_20220122_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', through='animeapp.AnimeFavoriteRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genres',
            field=models.ManyToManyField(related_name='genres', through='animeapp.AnimeGenreRelation', to='animeapp.Anime'),
        ),
    ]
