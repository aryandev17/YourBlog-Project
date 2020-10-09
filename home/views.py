from django.shortcuts import render, redirect, HttpResponse
from .models import Contact
from blog.models import Post

# Create your views here.
def home(request):
    post = Post.objects.all().order_by('-timestamp')
    context = {"posts":post}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contacts = Contact(name=name, email=email, message=message)
        contacts.save()

    return render(request, "home/index.html", context)

def about(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
        
    return render(request, "home/about.html")

