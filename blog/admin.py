from django.contrib import admin
from .models import Post, BlogComment

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("serial_no", "timestamp")

# Register your models here.

admin.site.register(Post)
admin.site.register(BlogComment, BlogCommentAdmin)