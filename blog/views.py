from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def blogHome(request):
    return HttpResponse("hello")

def blogPost(request):
    return HttpResponse("hello Post")