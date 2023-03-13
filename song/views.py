from django.shortcuts import render,redirect
from .forms import SongForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this


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
    
