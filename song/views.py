from django.shortcuts import render,redirect
from .forms import SongForm
from .forms import PodcastForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this
from .models import *

def index(request):
        music = Song.objects.all()
        songs = [music[i:i+3] for i in range(0, len(music), 3)] 
        return render(request, 'songs.html', {'songs': songs});

def podcasts(request):
        music = Podcast.objects.all()
        podcasts = [music[i:i+3] for i in range(0, len(music), 3)] 
        return render(request, 'podcasts.html', {'podcasts': podcasts});


def addSong(request):
    
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Uploaded successfully.")
            return redirect(".")
        messages.error(request, "Unsuccessful Uploadation. Invalid information.")
    form = SongForm()
    return render(request=request, template_name="addSong.html", context={"register_form": form})
    

def addPodcast(request):
    
    if request.method == "POST":
        form = PodcastForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Uploaded successfully.")
            return redirect("/song/podcasts")
        messages.error(request, "Unsuccessful Uploadation. Invalid information.")
    form = PodcastForm()
    return render(request=request, template_name="addPodcast.html", context={"register_form": form})
    

def songPage(request, song_id):
    targetSong = Song.objects.get(id = song_id)
    return render(request=request, template_name="songPage.html", context={"song": targetSong})

def podcastPage(request, podcast_id):
    targetPodcast = Podcast.objects.get(id = podcast_id)
    return render(request=request, template_name="podcastPage.html", context={"podcast": targetPodcast})

def likeSong(request, song_id):
    targetSong = Song.objects.get(id = song_id)
    targetSong.likeCount = targetSong.likeCount + 1
    targetSong.save()
    return render(request=request, template_name="songPage.html", context={"song": targetSong})

def likePodcast(request, podcast_id):
    targetPodcast = Podcast.objects.get(id = podcast_id)
    targetPodcast.likeCount = targetPodcast.likeCount + 1
    targetPodcast.save()
    return render(request=request, template_name="podcastPage.html", context={"podcast": targetPodcast})
    
    # link = "/song/song/" + str(song_id);
