# Urls for Blog App

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("postComment", views.postComment, name="postComment"),
    path("", views.blogHome, name="blogHome"),
    path("<str:category>", views.blogCat, name="blogHome"),
    path("<str:category>/<str:slug>", views.blogPost, name="blogPost")
]
