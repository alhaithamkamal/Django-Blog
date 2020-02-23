from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Post
from posts.form import PostForm

# Create your views here.
def posts(request):
    return render(request, 'homepage.html')

def post_detail(request):
	return render(request,"details.html",{})
def post_list(request):
	queryset=Post.objects.all()
	context={
	"objects_list":queryset,
	"title":'list'
	}
	return render(request,"index.html",context)
