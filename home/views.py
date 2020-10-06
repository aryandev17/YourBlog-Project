from django.shortcuts import render, redirect, HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contacts = Contact(name=name, email=email, message=message)
        contacts.save()

    return render(request, "home/index.html")

def about(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
        
    return render(request, "home/about.html")

