# tunr/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('songs/', views.song_list, name='song_list'),
]