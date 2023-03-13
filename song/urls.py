from django.urls import path
from . import views
app_name = "song"

urlpatterns = [
    path("addSong", views.addSong, name="home"),
]