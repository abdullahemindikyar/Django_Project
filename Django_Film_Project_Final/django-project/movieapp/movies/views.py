from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Category, Movie

kategori_liste = ["macera","romantik","dram","bilim kurgu"]
film_liste = [
    {
        "id": 1,
        "film_adi": "film 1",
        "aciklama": "film 1 açıklama",
        "resim": "1.jpeg",
        "anasayfa": True
    },
     {
        "id": 2,
        "film_adi": "film 2",
        "aciklama": "film 2 açıklama",
        "resim": "2.jpeg",
        "anasayfa": True
    },
    {
        "id": 3,
        "film_adi": "film 3",
        "aciklama": "film 3 açıklama",
        "resim": "3.jpeg",
        "anasayfa": False
    },
    {
        "id": 4,
        "film_adi": "film 4",
        "aciklama": "film 4 açıklama",
        "resim": "4.jpeg",
        "anasayfa": False
    }  
]

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(anasayfa=True)
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    movie = get_object_or_404(Movie, id=id)
    data = {
        "movie": movie,
        "is_favorite": movie.favoriler.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
        "is_liked": movie.begenenler.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
        "is_disliked": movie.begenmeyenler.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
    }
    return render(request, "details.html", data)

@login_required
def toggle_favorite(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if movie.favoriler.filter(id=request.user.id).exists():
        movie.favoriler.remove(request.user)
        is_favorite = False
    else:
        movie.favoriler.add(request.user)
        is_favorite = True
    return JsonResponse({'is_favorite': is_favorite})

@login_required
def toggle_like(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if movie.begenenler.filter(id=request.user.id).exists():
        movie.begenenler.remove(request.user)
        is_liked = False
    else:
        # Beğenmeyenler listesinden çıkar
        movie.begenmeyenler.remove(request.user)
        # Beğenenler listesine ekle
        movie.begenenler.add(request.user)
        is_liked = True
    return JsonResponse({'is_liked': is_liked})

@login_required
def toggle_dislike(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if movie.begenmeyenler.filter(id=request.user.id).exists():
        movie.begenmeyenler.remove(request.user)
        is_disliked = False
    else:
        # Beğenenler listesinden çıkar
        movie.begenenler.remove(request.user)
        # Beğenmeyenler listesine ekle
        movie.begenmeyenler.add(request.user)
        is_disliked = True
    return JsonResponse({'is_disliked': is_disliked})

@login_required
def favorite_movies(request):
    favori_filmler = request.user.favori_filmler.all()
    return render(request, 'favorites.html', {
        'favori_filmler': favori_filmler
    })