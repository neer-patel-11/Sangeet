from django.shortcuts import render,redirect
from .forms import SongForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this
from .models import *

def index(request):
        music = Song.objects.all()
        songs = [music[i:i+3] for i in range(0, len(music), 3)] 
        return render(request, 'home.html', {'songs': songs});



def addSong(request):
    
    # if request.method == "POST":
    #     form = SongForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         messages.success(request, "Registration successful.")
            # return redirect("login:home")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SongForm()
    return render(request=request, template_name="addSong.html", context={"register_form": form})
    
