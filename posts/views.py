from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Post , Comment
from .forms import PostCreateForm, PostEditForm, CommentForm
from django.http import HttpResponseRedirect



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
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		comment_form= CommentForm()		
	context = {
		'post' : post,
		'comments' : comments,
		'comment_form' : comment_form,
	}
	
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