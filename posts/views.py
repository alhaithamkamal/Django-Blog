from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Post , Comment
from .forms import *
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.urls import reverse



# Create your views here.


def posts(request):
    return render(request, 'homepage.html')



def post_list(request):
	post = Post.objects.all()
	context = {'post' : post}

	
	return render(request, 'post_list.html',context)


def post_detail(request,id):
	post = get_object_or_404(Post , id=id)
	comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = request.POST.get('content')
			reply_id = request.POST.get('comment_id')
			comment_qs = None
			if reply_id:
				comment_qs = Comment.objects.get(id=reply_id)	
			comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
			comment.save()
			#return HttpResponseRedirect(post.get_absolute_url())
	else:
		comment_form= CommentForm()		
	context = {
		'post' : post,
		'comments' : comments,
		'comment_form' : comment_form,
	}
	if request.is_ajax():
		html = render_to_string('post_detail', context, request=request)
		return JasonResponse({'form': html})
	
	return render(request,'post_detail.html',context)




def post_create(request):
	if request.method == 'POST':
		form= PostCreateForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.user = request.user
			post.save()

	else:
		form = PostCreateForm()
	context = {
		'form' : form,
	}

	return render(request, 'post_create.html' , context)





def user_login(request):
	if request.method == 'POST':
		Form = UserLoginForm(request.POST or None)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username , password=password)
			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('post_list'))
				else:
					return HttpResponseRedirect("User is not active")	
			else:
				return HttpResponseRedirect("User is None")
	else:
		form = UserLoginForm()

	context={
		'form' : form,
}
	return render(request, login.html, {'form' : form,})





def post_edit(request,id):
 	post =get_object_or_404(Post,id)
 	if request.method == 'POST':
 		form = PostEditForm(request.POST or None, instance=post)
 		if form.is_valid():
 			instance.save()
 			return HttpResponseRedirect(instance.get_absolut_url())
 	else:
 		form= PostEditForm()		
 	context = {
		
 		"title" :instance.title,
 		"post" : post,
 		"form" : form,}
			
 	return render(request, 'post_edit.html',context)



def like_post(request):
	post= get_object_or_404(Post, id=request.POST.get('post_id'))
	post.likes.add(request.user)
	return HttpResponseRedirect(post.get_absolute_url())




	post =get_object_or_404(Post,id)
	if request.method == 'POST':
		form = PostEditForm(request.POST or None, instance=post)
		if form.is_valid():
			instance.save()
			return HttpResponseRedirect(instance.get_absolut_url())
	else:
		form= PostEditForm()		
	context = {
		
		"title" :instance.title,
		"post" : post,
		"form" : form,}
			
	return render(request, 'post_edit.html',context)


# def DeletComment(request,id):
# 		#obj= get_object_or_404(Comment, id=id)
# 		try: 
# 			obj = Comment.objects.get(id=id)
# 		except:
# 			raise Http404

			
# 		if obj.user != request.user:
# 			#messages.success(request,"You don't have permission to view this.")
# 			#raise Http404
# 			reponse = HttpResponse("You don't have permission to view this")
# 			reponse.status_code = 403



# 		if request.method=="POST":
# 			parent_obj_url = obj.content_object.get_absolut_url()
# 			obj.delete()
# 			messages.success(request,"This has been deleted.")
# 			return HttpResponseRedirect(parent_obj_url)
# 		context={
# 			"object" : obj,

# 		}
# 		return render(request,"confirm_delete.html", context)





def commentEdit(request, id):
    post = get_object_or_404(Post,)
    comment = Comment.objects.get(id=id)
   
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('deletecomment')

    else:
    	form = CommentForm(instance = comment)

    return render (request, 'post_detail.html',{'form':form})       





def commentDelete (request,id):
	comment = 	Comment.objects.get(id = id)
	comment.delete()


	return HttpResponseRedirect('detail')
 	   






def commentCreate(request):
	if request.method =='POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect(post.get_absolute_url())

	else:
		form = CommentForm()


	return render(request,'post_detail.html', {'form' : form})
	


