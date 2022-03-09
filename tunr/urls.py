# tunr/urls.py
from django.urls import path
from . import views


urlpatterns = [
    #path for list page
    path('', views.artist_list, name='artist_list'),
    path('songs/', views.song_list, name='song_list'),
    #path for show page
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('songs/<int:pk>', views.song_detail, name='song_detail')
    #path for ...
    path('artists/new', views.artist_create, name='artist_create'),
]