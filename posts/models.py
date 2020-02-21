from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 30)
    user = models.ManyToManyField(User, blank=True)

    def __str__ (self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    tags = models.ManyToManyField('Tag')
    categories = models.ForeignKey(Category, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

