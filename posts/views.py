from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Tag, Category


@login_required
def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/homepage.html', context)