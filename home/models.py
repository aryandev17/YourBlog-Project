from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 5000, default="")
    email = models.EmailField(max_length=100)
    message = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = "user")