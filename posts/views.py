from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.views.generic import RedirectView
from posts.models import Post
from posts.form import PostForm
from django.contrib import messages


# Create your views here.
def posts(request):
    return render(request, 'homepage.html')

# to show the context of a post
def post_detail(request , num):
	instance = Post.objects.get(id= num)
	context ={'obj':instance}
	return render(request,'details.html',context)

#to show all the posts (just only published posts not the draft ) 
def post_list(request):
	queryset=Post.objects.all()
	context={
	"objects_list":queryset,
	"title":'list'
	}
	return render(request,"index.html",context)

# to update or edit the post
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


# to delete a post 
def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("../../posts/list")

# to create a post
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context= {
	"pt_form":form,
	}
	return render(request,"post_form.html",context) 

#to like the post if the user is not in like or dislike tables it will be added one like 
#if the user in one of the tables he must pressed one more time in the same button 

def like_post(request,id):
	post= get_object_or_404(Post, pk=id)
	postIsDisliked = post.dislikes.all()
	post_isliked = post.likes.all()
	user = request.user
	if (user not in  post_isliked):
		if(user not in postIsDisliked):
			post.likes.add(user)
			post.save()
	else:
		post.likes.remove(user)	
		post.save()				
	return HttpResponseRedirect("/posts/detail/"+id)

#to dislike the post if the user is not in like or dislike tables it will be added one dislike 
#if the user in one of the tables he must pressed one more time in the same button 

def dislike_post(request,id):
	post= get_object_or_404(Post, pk=id)
	postIsDisliked = post.dislikes.all()
	post_isliked = post.likes.all()
	user = request.user
	if (user not in  postIsDisliked):
		if(user not in post_isliked):
			post.dislikes.add(user)
			post.save()
	else:
		post.dislikes.remove(user)	
		post.save()
	
	total = post.dislikes.count()			
	if(total == 10):
		post.delete()
		return HttpResponse("<h1> this post has been deleted </h1>")				
	return HttpResponseRedirect("/posts/detail/"+id)
		
				
