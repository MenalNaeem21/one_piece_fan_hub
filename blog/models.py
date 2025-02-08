from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100000)
    created_at=models.DateTimeField(default=datetime.now,blank=True)

class Discussion(models.Model):
    title=models.CharField(max_length=300)    
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE) #user who created the post
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
class Comment(models.Model):
    discussion=models.ForeignKey(Discussion,on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    