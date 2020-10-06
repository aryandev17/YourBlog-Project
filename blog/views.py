from django.shortcuts import render, HttpResponse, redirect
from .models import Post

# Create your views here.

def blogHome(request):
    post = Post.objects.all()
    context = {"posts":post}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug):
    return HttpResponse("hello Post "+slug)