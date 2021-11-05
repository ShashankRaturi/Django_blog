from django.contrib import admin
from .models import Post

# Register your models here.

#if we want our model to appear in admin page , wer just have to register it here

admin.site.register(Post)