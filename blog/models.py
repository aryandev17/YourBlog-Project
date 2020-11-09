from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    serial_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, null=False)
    tagline = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=20, default="", null=False)
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to = "blog", blank= True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    serial_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
    
