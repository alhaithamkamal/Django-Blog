from .crud_users import *
from posts.models import Post, Tag, Category, Comment, Profanity
from posts.forms import PostForm, CommentForm, ProfanityForm, CategoryForm


""" the following views are to control users and admins 
    all the functions called here are implemented in crud_users.py file
    @author AbdAllah Zidan """

def users(request):
    return manager_show_normal_users(request)  

def admins(request):
    return manager_show_admins(request) 

def show(request,id):
    return manager_show_user(request,id) 

def lock(request , id):
    return manager_lock_user(request , id)
    
def delete(request,id):
    return manager_delete_user(request,id)

def unlock(request , id):
    return manager_unlock_user(request , id)

def promote(request , id):
    return manager_promote_user(request,id)

def demote(request , id):
    return super_demote_admin(request , id)

def lock_admin(request,id):
    return super_lock_admin(request,id)

def unlock_admin(request , id):
    return super_unlock_admin(request , id)

def delete_admin(request , id):
    return super_delete_admin(request , id)

""" end of users control views """ 

""" statrrt of posts control views """ 
def posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    profane_words = Profanity.objects.all()
    context = {'posts': posts, 'categories': categories, 'profane_words': profane_words}
    return render(request, 'manager/landing.html', context)

def post_delete(request, post_id):
	post = Post.objects.get(id=post_id)
	post.delete()
	return HttpResponseRedirect('/manager/')

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manager')
    else:
        context = {"pt_form": form}
        return render(request,"form.html",context)

def delete_category(request, cat_id):
    category = Category.objects.get(id=cat_id)
    category.delete()
    return HttpResponseRedirect('/manager')

def add_profane_word(request):
    form = ProfanityForm()
    if request.method == 'POST':
        form = ProfanityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manager')
    else:
        context = {"pt_form": form}
        return render(request,"form.html",context)
def delete_profane_word(request, id):
    profane_word = Profanity.objects.get(id=id)
    profane_word.delete()
    return HttpResponseRedirect('/manager')