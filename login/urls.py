from django.urls import path
from . import views
app_name = "login"

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("logintemplate", views.login_request, name="logintemplate"),
    path("",views.home,name="home"),
    path("logout", views.logout_request, name="logout"),
]