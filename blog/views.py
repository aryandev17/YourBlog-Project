from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages

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

def blogPost(request, category, slug):
    post = Post.objects.filter(slug= slug, category=category).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.serial_no not in replyDict.keys():
            replyDict[reply.parent.serial_no] = [reply]
        else:
            replyDict[reply.parent.serial_no].append(reply)
    context = {"post":post, "comments":comments, "replyDict":replyDict}
    return render(request, "blog/post.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment-textarea")
        user = request.user
        postSerial = request.POST.get("postSerial")
        parentSerial = request.POST.get("parentSerial")
        post = Post.objects.get(serial_no = postSerial)

        if parentSerial == "":
            comment = BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your Comment has been Sent !!")

        else:
            parentComment = BlogComment.objects.filter(serial_no= parentSerial)
            comment = BlogComment(comment= comment, user=user, post=post, parent=parentComment)
            comment.save()
            messages.success(request, "Your Reply has been Sent !!")

    return redirect(f"/blog/{post.category}/{post.slug}")