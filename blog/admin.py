from django.contrib import admin

# Register your models here.

from .models import BlogPost

# Register the database in the admin
admin.site.register(BlogPost)

