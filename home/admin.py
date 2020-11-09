from django.contrib import admin
from .models import Contact, Profile

class ContactAdmin(admin.ModelAdmin):
    list_display = ("serial_no", "name", "email", "message")

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile)