from django.shortcuts import render

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
