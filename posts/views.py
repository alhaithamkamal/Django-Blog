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
	instance =get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()



	context = {
		
		"title" :instance.title,
		"instance" : instance,
		"pt_form" : form,}
			
	return render(request, 'post_form.html',context)
	# st= Post.objects.get(id = num)
	# if request.method == 'POST':
	# 	form = PostForm(request.POST,instance=st)
	# 	if form.is_valid():
	# 		form.save()
	# 		return HttpResponseRedirect('homepage.html')

	# else:
	# 	form = PostForm(instance=st)
	# 	context = {'pt_form': form}
	# 	return render(request,'post_form.html', context)


   
def post_delete(request, num):
	instance = Post.objects.get(id=num)
	instance.delete()
	# messages.success(request,"deleted Successly")
	# return redirect("Posts:list")
	return HttpResponseRedirect('homepage.html')

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context= {
	"pt_form":form,
	}
	return render(request,"post_form.html",context)
	

			
	