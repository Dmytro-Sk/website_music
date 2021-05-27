from django.shortcuts import render
from django.http import HttpResponse

from .models import Album


def index(request):
    all_albums = Album.objects.all()
    http = ''
    for album in all_albums:
        http += f'<a href="{album.id}">{album.album_title}</a><br>'
    return HttpResponse(http)


def detail(request, album_id):
    return HttpResponse(
        f'<br><br><h1 style="text-align:center; background-color: powderblue">It\'s detail to album {album_id}</h1>'
    )
