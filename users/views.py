from django.shortcuts import render 
from django.http import  HttpResponseRedirect
from .forms import RegistrationForm , ProfileForm , LoginForm
from .util_funcs import isLocked 
from posts  import views as post_views
from .models import Profile
from django.contrib.auth import login , authenticate
from .logger import log

def register(request):
    if(not request.user.is_authenticated):
        if request.method == "POST":
            user_form = RegistrationForm(request.POST)
            profile_form = ProfileForm(request.POST, request.FILES ) # get the form and the upladed files
            print("form valid : ",user_form.is_valid()) # for debugging purposes
            print("pic valid : ",profile_form.is_valid()) # for debugging purposes
            if user_form.is_valid() : 
                user =user_form.save() # save the user into database and return it 
                profile=Profile.objects.get(user = user) # get the profile of the created user
                file =request.FILES.get("profile_pic") # get the uplloaded picture if any
                if(file != None):
                    profile.profile_pic = file # add the provided pic to that user profile
                profile.save() # save the updates to user profile
                log("created")  # for debugging purposes
                user = authenticate(username=request.POST["username"] , password =  request.POST["password1"] )
                if user is not None:
                    login(request , user)
                else:
                    log("cannot login from refistration form")
                return HttpResponseRedirect("/users/profile") # redirect to user profile page
            else:
                log("invalid registration form") # for debugging purposes          
        else:
            user_form = RegistrationForm()
            profile_form = ProfileForm()
        context = {"user_form":user_form,"profile_form":profile_form}
        return render(request , 'users/register.html',context)
    else:
        return HttpResponseRedirect("/")


def profile(request):
    user = request.user  # get the current user
    userprofile = Profile.objects.get(user=user)  # get the profile related to that user
    context = {"user":user,"userprofile":userprofile }
    return render(request , "users/profile.html",context)

def blocked(request):
    # this view will be fired when a locked user tries to login
    return render(request,"users/blocked.html")

def login_view(request):
    if(not request.user.is_authenticated): # check if user is already logged in
        if request.method == "POST": 
            login_form = LoginForm(data=request.POST) # using named parameter as request.Post isn't the first parameter by default
            if(login_form.is_valid()):
                username = request.POST['username']
                password = request.POST["password"]
                user = authenticate(username=username , password = password) # authenticate the user with provided data
                if user is not None: #user authenticated
                    if(isLocked(user)): 
                        log(user.username +"blocked user")
                        return HttpResponseRedirect("/users/blocked") #redirect the user to a custom page for blocked users   
                    else:
                        login(request , user)
                        log(user.username +"logged in successfully") 
                else:
                    log("cannot login from login page")
                return HttpResponseRedirect("/") # redirect to user homepage
            else:
                log("invalid login form")
        else:
            login_form = LoginForm()
        context = {"login_form":login_form}
        return render(request , 'users/login.html',context)
    else:
        return HttpResponseRedirect("/")


