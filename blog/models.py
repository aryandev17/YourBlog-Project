from django.db import models
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    serial_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, null=False)
    tagline = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=20, default="", null=False)
    category_color_code_or_color_name = models.CharField(max_length = 7, default="Example - #0000FF or Blue")
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to = "blog")
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.title + " by " + self.author


