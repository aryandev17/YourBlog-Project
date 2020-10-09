from django.shortcuts import render, HttpResponse, redirect
from .models import Post

# Create your views here.

def blogHome(request):
    post = Post.objects.all()
    print(post)
    context = {"posts":post, "categories":post}
    return render(request, "blog/blogHome.html", context)

def blogCat(request, category):
    post = Post.objects.filter(category=category)
    categories = Post.objects.all()
    print(post)
    context = {"posts":post, "categories":categories}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug):
    return HttpResponse("hello Post "+slug)