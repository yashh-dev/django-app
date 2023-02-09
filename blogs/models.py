from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    likes=models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)