from django.urls import path, include
from . import views
import debug_toolbar  # 追加
from django.conf import settings

urlpatterns = [
	path('index', views.index, name='index'),
	path('anime', views.anime_list, name='anime'),
	path('anime/<int:anime_id>', views.favorite, name='favorite'),
	path('anime-upload', views.anime_upload, name='anime-upload'),
	path('genre-upload', views.genre_upload, name='genre-upload'),
	path('anime-genre-upload', views.anime_genre_upload, name='anime-genre-upload'),
	path('login/', views.Login.as_view(), name='login'),
	path('logout/', views.Logout.as_view(), name='logout'),
	path('signup', views.signup, name='signup'),
	path('delete-favorite', views.delete_favorite, name='delete-favorite'),
]

if settings.DEBUG:
	urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]