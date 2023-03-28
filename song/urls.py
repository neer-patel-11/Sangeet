from django.urls import path
from . import views

app_name = "song"

urlpatterns = [
    path("addSong", views.addSong, name="addSong"),
    path("addPodcast", views.addPodcast, name="addPodcast"),
    path("", views.index, name="index"),
    path("podcasts", views.podcasts, name="podcasts"),
    path("song/<int:song_id>", views.songPage, name="songPage"),
    path("songPage/<int:song_id>", views.likeSong, name="likeSong"),
    path("podcastPage/<int:podcast_id>", views.likePodcast, name="likePodcast"),
    path("podcasts/<int:podcast_id>", views.podcastPage, name="podcastPage"),
]
