from django.urls import path

from . import views

app_name = 'music'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='detail'),
    path('album/add/', views.AlbumCreateView.as_view(), name='album-add'),
]
