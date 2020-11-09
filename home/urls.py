# Urls for Home App

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signupUser, name="signup"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("editPost/<str:serial_no>", views.editPost, name="editPost"),
    path("deletePost/<str:slug>", views.deletePost, name="deletePost")
]