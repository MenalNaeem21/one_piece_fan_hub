from django.contrib import admin
from .models import Post
from .models import Discussion, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Discussion)
admin.site.register(Comment)

