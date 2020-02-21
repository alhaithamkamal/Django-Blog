from django.shortcuts import render
from .models import Post, Tag, Category

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'homepage.html', context)
