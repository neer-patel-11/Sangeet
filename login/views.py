from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import UserForm
from django.contrib import messages
from django.http import HttpResponse

from .models import Users

def home(request):
    return render(request, 'home.html')

def register_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            return redirect("login:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":    
        password=request.POST['password']
        username=request.POST['username']
        user=Users.objects.get(username=username,password=password)
        if user is not None:
            request.session['username']=username
            request.session['password']=password
            return HttpResponseRedirect("/login/")
    return render(request=request, template_name="logintemplate.html")

def logout_request(request):
    request.session.flush()
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect("/login/logintemplate")



