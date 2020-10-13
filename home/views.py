from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve

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

def signupUser(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        userSignup = request.POST.get("userSignup")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if len(userSignup) > 10:
            messages.error(request, "Username Must be less than 10 Characters and must be alphanumeric !!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if password1 != password2:
            messages.error(request, "Passwords must be same !!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        newUser = User.objects.create_user(userSignup, email, password1)
        newUser.first_name = fname
        newUser.last_name = lname
        newUser.save()
        messages.success(request, "Your account has been Created !!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse("signup")

def loginUser(request):
    if request.method == "POST":
        userLogin = request.POST.get("userLogin")
        password = request.POST.get("password")

        user = authenticate(username = userLogin, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Please Enter the Valid Credentials !!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return HttpResponse("login")

def logoutUser(request):
    logout(request)
    messages.success(request, "You are logged Out !!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))