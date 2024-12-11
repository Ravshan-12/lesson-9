from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie


def home(request):
    return render(request, 'index.html')


def movie_lis(request):
    movies = Movie.objects.all()
    ctx = {'movies':movies}
    return render(request, 'movies/list.html', ctx)


def movie_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        if title and director and release_year and genre:
            Movie.objects.create(
                title = title,
                director = director,
                release_year = release_year,
                genre = genre

            )
            return redirect('movies:list')
    return render(request, 'movies/form.html')


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ctx = {'movie': movie}
    return render(request, 'movies/detail.html', ctx)


def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('movies:list')


def movie_update(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        if title and director and release_year and genre:
            movie.title = title
            movie.director = director
            movie.release_year = release_year
            movie.genre = genre
            movie.save()
            return redirect(movie.get_detail_url())
    ctx = {'movie': movie}
    return render(request, 'movies/form.html', ctx)