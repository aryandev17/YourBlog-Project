from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve
from django.core.files.storage import FileSystemStorage
from blog.forms import ImageForm
from django.utils.timezone import datetime

# Create your views here.
def home(request):
    post = Post.objects.all().order_by('-timestamp')
    context = {"posts":post}

    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
        messages.success(request, "Your Message has been Sent :)")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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
        user = authenticate(username = userSignup, password = password1)
        login(request, user)
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

def dashboard(request):
    post = Post.objects.all()
    context = {"posts":post}
    return render(request, "blog/dashboard.html", context)

def editPost(request, serial_no):
    if request.method == "POST":
        title = request.POST.get("title")
        tagline = request.POST.get("tagline")
        post_slug = request.POST.get("slug")
        content = request.POST.get("content")
        author = request.user
        category = request.POST.get("category")
        timestamp = datetime.now()

        imageForm = ImageForm(request.POST, request.FILES)

        if serial_no == "0":

            if imageForm.is_valid():
                formImage = imageForm.cleaned_data["image"]
                new_post = Post(title=title, tagline=tagline, slug=post_slug, content=content, author=author, category=category, timestamp=timestamp, thumbnail_image=formImage)
            else:
                new_post = Post(title=title, tagline=tagline, slug=post_slug, content=content, author=author, category=category, timestamp=timestamp)

            new_post.save()
            return redirect("/dashboard")
            
        else:
            
            if imageForm.is_valid():
                formImage = imageForm.cleaned_data["image"]
                post = Post.objects.filter(serial_no= serial_no).first()
                post.thumbnail_image = formImage
            else:
                post = Post.objects.filter(serial_no= serial_no).first() 
            
            post.title = title
            post.tagline = tagline
            post.slug = post_slug
            post.content = content
            post.category = category
            post.save()
            return redirect(f"/editPost/{serial_no}")

    else:
        imageForm = ImageForm()
            
    post = Post.objects.filter(serial_no= serial_no).first()
    context = {"post":post, "serial_no":serial_no, "form":imageForm}
    return render(request, "blog/editPost.html", context)

def deletePost(request, slug):
    post = Post.objects.get(slug = slug)
    post.delete()
    return redirect("/dashboard")