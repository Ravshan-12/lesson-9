from django.shortcuts import render, redirect, get_object_or_404
from .models import Song


def home(request):
    return render(request, 'index.html')


def music_lis(request):
    music = Song.objects.all()
    ctx = {'music':music}
    return render(request, 'music/list.html', ctx)


def music_create(request):
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        if album_title and artist and release_date and genre:
            Song.objects.create(
                album_title = album_title,
                artist = artist,
                release_date = release_date,
                genre = genre

            )
            return redirect('music:list')
    return render(request, 'music/form.html')


def music_detail(request, music_id):
    song = get_object_or_404(Song, pk=music_id)
    ctx = {'song': song}
    return render(request, 'music/detail.html', ctx)


def music_delete(request, music_id):
    song = get_object_or_404(Song, pk=music_id)
    song.delete()
    return redirect('music:list')


def music_update(request, music_id):
    song = get_object_or_404(Song, pk=music_id)
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        if album_title and artist and release_date and genre:
            song.album_title = album_title
            song.artist = artist
            song.release_date = release_date
            song.genre = genre
            song.save()
            return redirect(song.get_detail_url())
    ctx = {'song': song}
    return render(request, 'music/form.html', ctx)