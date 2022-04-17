from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    anime_name = models.CharField('アニメ名', max_length=100)
    type = models.CharField('タイプ', max_length=30)
    rating = models.FloatField('評価')
    members = models.PositiveIntegerField('評価者数')
    favorites = models.ManyToManyField(User, through='AnimeFavoriteRelation', related_name='favorites')

    def __str__(self):
        return self.anime_name

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    genre_name = models.CharField('ジャンル名', max_length=30)
    genre = models.ManyToManyField(Anime, through='AnimeGenreRelation', related_name='genres')

    def __str__(self):
        return self.genre_name

class AnimeGenreRelation(models.Model):
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE)
    ganre_id = models.ForeignKey('Genre', on_delete=models.CASCADE)

class Rationg(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    rating = models.FloatField('評価')

class AnimeFavoriteRelation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)