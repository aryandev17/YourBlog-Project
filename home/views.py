from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

