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


   
# def post_delete(request, num):
# 	instance = Post.objects.get(id=num)
# 	instance.delete()
# 	messages.success(request,"deleted Successly")
# 	# return redirect("Posts:list")
# 	return HttpResponseRedirect('homepage.html')


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

# like or dislike post
 
# def like_post(request,id):
# 	post= get_object_or_404(Post, pk=id)
# 	post.likes.add(request.user)
# 	post.save()
# 	return HttpResponseRedirect("/posts/detail/"+id)


# def like_post(request,id):
# 	post= get_object_or_404(Post, pk=id)
# 	for p in post.likes.all():
# 		if (request.user==post.user):
# 			post.likes.remove(post.user)
# 			post.save()
# 		else:
# 			post.likes.add(request.user)
# 			post.save()
# 	return HttpResponseRedirect("/posts/detail/"+id)



# def like_post(request,id):
# 	post= get_object_or_404(Post, pk=id)
# 	post_u = post.likes.all()
# 	for p in post_u:
# 		if (request.user in post_u):
# 			post.likes.remove(request.user in post_u)
# 			post.save()
# 		else:
# 			post.likes.add(request.user)
# 			post.save()
# 	return HttpResponseRedirect("/posts/detail/"+id)


def like_post(request,id):
	post= get_object_or_404(Post, pk=id)
	post_u = post.likes.all()
	post_d = post.dislikes.all()
	for p in post_d:
		if (request.user not in post_d):
			for p in post_u:
				if (request.user in  post_u):
					post.likes.remove(request.user in post_u)
					post.save()
				else:
					post.likes.add(request.user)
					post.save()
	return HttpResponseRedirect("/posts/detail/"+id)

def dislike_post(request,id):
	post= get_object_or_404(Post, pk=id)
	post_d = post.dislikes.all()
	post_u = post.likes.all()
	for pt in post_u:
		if (request.user not in  post_u):
			for p in post_d:
				if (request.user in post_d):
					po=request.user in post_d
					post.dislikes.remove(po)
					post.save()
				else:
					post.dislikes.add(request.user)
					post.save()
	total = post.dislikes.count()			
	if(total == 2):
		post.delete()
		return HttpResponse("<h1> this post has been deleted </h1>")				
	return HttpResponseRedirect("/posts/detail/"+id)
		
				
