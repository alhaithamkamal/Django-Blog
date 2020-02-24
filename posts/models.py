from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural="Categories"

class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def snippet(self):
        return self.body[:50]+"..."

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
