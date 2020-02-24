from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Post
from posts.form import PostForm
from django.contrib import messages


# Create your views here.
def posts(request):
    return render(request, 'homepage.html')


def post_detail(request , num):
	instance = Post.objects.get(id= num)
	context ={'obj':instance}
	return render(request,'details.html',context)

def post_list(request):
	queryset=Post.objects.all()
	context={
	"objects_list":queryset,
	"title":'list'
	}
	return render(request,"index.html",context)


def post_update(request, id):
	post=get_object_or_404(Post,id=id)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()	
		return HttpResponseRedirect('/posts')
	else:
		form = PostForm(instance=post)
		context = {"pt_form": form}
		return render(request,"post_form.html",context)

def post_delete(request, num):
	instance = Post.objects.get(id=num)
	instance.delete()
	# return redirect("Posts:list")
	return HttpResponseRedirect('/posts')

def post_create(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return HttpResponseRedirect('/posts')
	else:
		context = {"pt_form": form}
		return render(request,"post_form.html",context)