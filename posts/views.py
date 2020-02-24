from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import Post, Tag, Category
from django.db.models import Q
from django.shortcuts import render ,get_object_or_404
from posts.form import PostForm

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
    return render(request, 'home.html', context)

def post_detail(request , post_id):
    categotries = Category.objects.all()
    tags = Tag.objects.all()[:10]
    user = request.user
    post = Post.objects.get(id= post_id)
    context = {'post': post, 'categories': categotries,'tags': tags, 'user': user}
    return render(request,'single.html', context)

def subscribe(request, cat_id):
    user = request.user
    category = Category.objects.get(id=cat_id)
    category.user.add(user)
    return HttpResponseRedirect('/')

def unsubscribe(request, cat_id):
    user = request.user
    category = Category.objects.get(id=cat_id)
    category.user.remove(user)
    return HttpResponseRedirect('/')

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
    return render(request, 'home.html', context)

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
    return render(request, 'home.html', context)

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
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def post_update(request, id):
	post=get_object_or_404(Post,id=id)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()	
		return HttpResponseRedirect('/')
	else:
		form = PostForm(instance=post)
		context = {"pt_form": form}
		return render(request,"post_form.html",context)

def post_delete(request, num):
	instance = Post.objects.get(id=num)
	instance.delete()
	# return redirect("Posts:list")
	return HttpResponseRedirect('/')

def post_create(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return HttpResponseRedirect('/')
	else:
		context = {"pt_form": form}
		return render(request,"post_form.html",context)
