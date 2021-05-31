from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Album


class IndexListView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'  # default 'object_list'

    def get_queryset(self):
        return Album.objects.all()


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')  # or success_url = '/music/'
