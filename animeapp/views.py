from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from io import TextIOWrapper, StringIO
import csv
from .models import Anime, Genre, AnimeGenreRelation, AnimeFavoriteRelation, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import pickle
import joblib
import pandas as pd

loaded_model = joblib.load('model/model.joblib')
df = joblib.load('model/df_normal.joblib')
df_piv = df.pivot(index="anime_id",columns="user_id",values="rating").fillna(0)

@login_required
def index(request):
    return render(request, 'animeapp/index.html')

@login_required
def anime_list(request):
	anime_list = Anime.objects.order_by('members').reverse()
	anime_list_page = paginate_query(request, anime_list, settings.PAGE_PER_ITEM)
	return render(request, 'animeapp/list.html', context={
		'anime_list':anime_list_page,
	})

@login_required
def anime_upload(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		header = next(csv_file)
		for line in csv_file:
			anime = Anime()
			anime.id = line[1]
			anime.name = line[2]
			anime.type = line[4]
			anime.rating = line[6]
			anime.members = line[7]
			anime.save()
		return render(request, 'animeapp/anime_upload.html')
	else:
		return render(request, 'animeapp/anime_upload.html')

@login_required
def genre_upload(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		header = next(csv_file)
		for line in csv_file:
			genre = Genre()
			genre.id = line[0]
			genre.name = line[1]
			genre.save()
		return render(request, 'animeapp/anime_upload.html')
	else:
		return render(request, 'animeapp/anime_upload.html')

@login_required
def anime_genre_upload(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		header = next(csv_file)
		for line in csv_file:
			anime_genre = AnimeGenreRelation()
			anime = Anime()
			genre = Genre()
			# anime_genre.anime_id = line[1]
			anime_genre.anime_id = Anime.objects.get(id=line[1])
			anime_genre.ganre_id = Genre.objects.get(id=line[2])
			# anime_genre.ganre_id = line[2]
			anime_genre.save()
		return render(request, 'animeapp/anime_upload.html')
	else:
		return render(request, 'animeapp/anime_upload.html')

# ページネーション用に、Pageオブジェクトを返す。
def paginate_query(request, queryset, count):
	paginator = Paginator(queryset, count)
	page = request.GET.get('page')
	try:
		page_obj = paginator.page(page)
	except PageNotAnInteger:
		page_obj = paginator.page(1)
	except EmptyPage:
		page_obj = paginatot.page(paginator.num_pages)
	return page_obj

@login_required
def favorite(request, anime_id):
	if request.method == 'POST' and request.is_ajax() == False:
		user = User(id=request.user.id)
		anime = Anime(id=anime_id)
		anime_favorite = AnimeFavoriteRelation(user_id=user, anime_id=anime)
		anime_favorite.save()

		distance, indice = loaded_model.kneighbors(df_piv.iloc[df_piv.index== anime_id].values.reshape(1,-1), n_neighbors=11)
		recommend_anime_list = []
		for i in range(11):
			if  i == 0:
				continue
			else:
				recommend_anime_list.append(df_piv.index[indice.flatten()[i]])
		anime_list = Anime.objects.filter(id__in=recommend_anime_list)
		return render(request, 'animeapp/recommend.html', context={'anime_list':anime_list})
	else:
		anime_list = Anime.objects.order_by('members').reverse()
		anime_list_page = paginate_query(request, anime_list, settings.PAGE_PER_ITEM)   # ページネーション
		return render(request, 'animeapp/list.html', context={'anime_list':anime_list_page})

# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'animeapp/login.html'

class Logout(LogoutView):
    template_name = 'animeapp/base.html'

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#フォームから'username'を読み取る
			username = form.cleaned_data.get('username')
			#フォームから'password1'を読み取る
			password = form.cleaned_data.get('password1')
			# 読み取った情報をログインに使用する情報として new_user に格納
			new_user = authenticate(username=username, password=password)
			if new_user is not None:
				# new_user の情報からログイン処理を行う
				login(request, new_user)
			# ログイン後のリダイレクト処理
			return redirect('index')
	# POST で送信がなかった場合の処理
	else:
		form = SignUpForm()
		return render(request, 'animeapp/signup.html', {'form': form})

def delete_favorite(request):
	if request.method =="POST" and request.is_ajax():
		anime = get_object_or_404(Anime, pk=request.POST.get('anime_id'))
		user = User(id=request.user.id)
		favorite = AnimeFavoriteRelation.objects.filter(anime_id=anime, user_id=user)
		if favorite.exists():
			favorite.delete()
		context={
			'anime_id': anime.id,
		}
		return JsonResponse(context)