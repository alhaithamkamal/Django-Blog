from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post, Tag, Category
from django.db.models import Q

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categotries = Category.objects.all()
    tags = Tag.objects.all()[:10]
    user = request.user
    context = {'page_obj': page_obj, 'categories': categotries,'tags': tags, 'user': user}
    return render(request, 'index.html', context)

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

def categoryPosts(request, cat_id):
    category = Category.objects.get(id=cat_id)
    posts = Post.objects.filter(category=category)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categotries = Category.objects.all()
    tags = Tag.objects.all()[:10]
    user = request.user
    context = {'page_obj': page_obj, 'categories': categotries,'tags': tags, 'user': user}
    return render(request, 'index.html', context)

def tagPosts(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    posts = tag.post_set.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categotries = Category.objects.all()
    tags = Tag.objects.all()[:10]
    user = request.user
    context = {'page_obj': page_obj, 'categories': categotries,'tags': tags, 'user': user}
    return render(request, 'index.html', context)

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query))
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categotries = Category.objects.all()
    tags = Tag.objects.filter(Q(name__icontains=query))[:10]
    user = request.user
    context = {'page_obj': page_obj, 'categories': categotries,'tags': tags, 'user': user}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
