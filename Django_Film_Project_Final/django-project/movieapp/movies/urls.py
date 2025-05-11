from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/4
# http://127.0.0.1:8000/arka-sokaklar

app_name = 'movies'

urlpatterns = [
    path('', login_required(views.movies), name='movie_list'),  # Film listesi
    path('home/', login_required(views.home), name='home'),  # Ana sayfa filmleri
    path('movie/<int:id>', login_required(views.moviedetails), name='movie_details'),  # Film detayları
    path('movie/<int:movie_id>/favorite/', login_required(views.toggle_favorite), name='toggle_favorite'),
    path('movie/<int:movie_id>/like/', login_required(views.toggle_like), name='toggle_like'),
    path('movie/<int:movie_id>/dislike/', login_required(views.toggle_dislike), name='toggle_dislike'),
    path('favorites/', login_required(views.favorite_movies), name='favorite_movies'),
]