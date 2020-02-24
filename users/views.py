from django.shortcuts import render 
from django.http import  HttpResponseRedirect
from .forms import RegistrationForm , ProfileForm , LoginForm , EditProfileForm , ChangePasswordForm
from .util_funcs import isLocked 
from posts  import views as post_views
from .models import Profile
from django.contrib.auth import login , authenticate ,  update_session_auth_hash
from django.contrib.auth.models import User
from .logger import log
from django.core.mail import send_mail
from .util_funcs import delete_profile_pic
import os

def register(request):

    """this custom login view does the following:
    1- checks if request comes from an already logged in user so it redirects him to hompage again
    2- check if the method is post and then the submitted form is valid
    3- saves the user data and his profile data
    4- login the user and redirects him to profile page in case of success"""

    if(not request.user.is_authenticated):
        if request.method == "POST":
            user_form = RegistrationForm(request.POST)
            profile_form = ProfileForm(request.POST, request.FILES ) # get the form and the upladed files
            if user_form.is_valid() : 
                user =user_form.save() # save the user into database and return it 
                profile=Profile.objects.get(user = user) # get the profile of the created user
                file =request.FILES.get("profile_pic") # get the uplloaded picture if any
                if(file != None):
                    profile.profile_pic = file # add the provided pic to that user profile
                profile.bio =request.POST["bio"]
                profile.save() # save the updates to user profile
                log("created a new user successfully with username: "+user.username)  # for debugging purposes
                user = authenticate(username=request.POST["username"] , password =  request.POST["password1"] )
                if user is not None:
                    login(request , user)
                    try:
                        send_mail('Welcome to our blog','Django Blog team welcomes you to our blog .','DjangoTeam@django.com',[user.email],fail_silently=False,)
                    except Exception as ex:
                        log("couldn't send email message"+str(ex))
                    
                    return HttpResponseRedirect("/users/profile") # redirect to user profile page
                else:
                    log("cannot login from refistration form")              
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
    if(not request.user.is_authenticated):
        admins = User.objects.all().filter(is_staff__exact=True)
        return render(request,"users/blocked.html",{"admins":admins})
    return HttpResponseRedirect("/")
    
def login_view(request):

    """this custom login view does the following:
    1- checks if request comes from an already logged in user so it redirects him to hompage again
    2- check if the method is post and then the submitted form is valid
    3- check if the credentials are correct using authenticate method 
    4- check if user isn't registered takes him back to login back
    5- if user is registered but locked redirects him to blocked page"""

    if(not request.user.is_authenticated): # check if user is already logged in
        if request.method == "POST": 
            login_form = LoginForm(data=request.POST) # using named parameter as request.Post isn't the first parameter by default
            if(login_form.is_valid()):
                username = request.POST['username']
                password = request.POST["password"]
                user = authenticate(username=username , password = password) # authenticate the user with provided data
                if user is not None: #user authenticated
                    if(isLocked(user)): 
                        log(user.username +" blocked user")
                        return HttpResponseRedirect("/users/blocked") #redirect the user to a custom page for blocked users   
                    else:
                        login(request , user)
                        log(user.username +" logged in successfully") 
                        return HttpResponseRedirect("/") # redirect to user homepage
                else:
                    log("cannot login from login page")
                
            else:
                log("invalid login form")
        else:
            login_form = LoginForm()
        context = {"login_form":login_form}
        return render(request , 'users/login.html',context)
    else:
        return HttpResponseRedirect("/")


def edit_profile(request):

    """this edit profile view does the following:
    1- checks that user is logged in already or redirects him to homepage
    2- check if the method is post and then the submitted forms are valid
    3- update user info and save
    4- if success redirects the user to profile page"""

    if(request.user.is_authenticated):
        if request.method == "POST":
            edit_form = EditProfileForm(data=request.POST)
            profile_form = ProfileForm(request.POST, request.FILES )
            user = request.user
            if(edit_form.is_valid()):
                log("valid edit form")
                file =request.FILES.get("profile_pic")
                user.first_name=request.POST["first_name"]
                user.last_name=request.POST["last_name"]
                user.profile.bio = request.POST["bio"]
                if(file != None):
                    if(user.profile.profile_pic !=None):
                        delete_profile_pic(user.profile.profile_pic)
                    user.profile.profile_pic = file
                user.save()
                user.profile.save()
                log(user.username + "  updated his profile")
                return HttpResponseRedirect("/users/profile")
            else:
                log("invalid change form")
                return HttpResponseRedirect("/")
        else:
            user =request.user
            user_data = {"first_name":user.first_name ,"last_name":user.last_name }
            bio_data ={"bio":user.profile.bio}
            edit_form = EditProfileForm(data=user_data)
            profile_form = ProfileForm(data=bio_data)
            context = {"edit_form":edit_form , "profile_form":profile_form}
            return render(request , "users/edit.html" , context)
    else:
        return HttpResponseRedirect("/")

def change_password(request):

    """this change password view does the following:
    1- checks that user is logged in already or redirects him to homepage
    2- check if the method is post and then the submitted forms are valid
    3- update user password and save
    4- if success redirects the user to profile page"""

    if(request.user.is_authenticated):
        if request.method == 'POST':
            form = ChangePasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user) 
                log("changed password for "+user.username)
                return HttpResponseRedirect('/users/profile')
            else:
                log("couldn't change password for "+user.username)
        else:
            form = ChangePasswordForm(request.user)
        return render(request, 'users/change_password.html', {
            'form': form
        })
    else:
        return HttpResponseRedirect("/")


