from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post, Tag, Category

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    categotries = Category.objects.all()
    user = request.user
    context = {'posts': posts, 'categories': categotries, 'user': user}
    return render(request, 'homepage.html', context)

def subscribe(request, cat_id):
    user = request.user
    category = Category.objects.get(id=cat_id)
    category.user.add(user)
    return HttpResponseRedirect('/posts')

def unsubscribe(request, cat_id):
    user = request.user
    category = Category.objects.get(id=cat_id)
    category.user.remove(user)
    return HttpResponseRedirect('/posts')