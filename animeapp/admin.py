from django.contrib import admin
from .models import Anime, Genre, AnimeGenreRelation, Rationg, AnimeFavoriteRelation


admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(AnimeGenreRelation)
admin.site.register(Rationg)
admin.site.register(AnimeFavoriteRelation)
