from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import UserForm
from django.contrib import messages
from django.http import HttpResponse

from .models import Users


def register_request(request):
    message=None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            return redirect("/login/logintemplate")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        message="Unsuccessful registration. Invalid information."
    form = UserForm()
    return render(request=request, template_name="register.html", context={"register_form": form , 'message':message})

def login_request(request):
    if request.method == "POST":    
        password=request.POST['password']
        username=request.POST['username']
        user=Users.objects.get(username=username)
        if user is not None and user.password==password:
            request.session['username']=username
            request.session['password']=password
            return HttpResponseRedirect("/song/")
    return render(request=request, template_name="logintemplate.html")

def logout_request(request):
    request.session.flush()
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect("/login/logintemplate")



