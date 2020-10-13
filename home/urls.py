# Urls for Home App

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("signup/", views.signupUser, name="signup"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout")
]