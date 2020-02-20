from django.shortcuts import render 
from django.http import  HttpResponseRedirect
from .forms import RegistrationForm , ProfileForm
from posts  import views as post_views
from .models import Profile
from django.contrib.auth import login , authenticate
from .logger import log

def register(request):
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
                log("cannot login")
            return HttpResponseRedirect("/users/profile") # redirect to user profile page
        else:
            log("invalid") # for debugging purposes          
    else:
        user_form = RegistrationForm()
        profile_form = ProfileForm()
    context = {"user_form":user_form,"profile_form":profile_form}
    return render(request , 'users/register.html',context)


def profile(request):
    user = request.user
    userprofile = Profile.objects.get(user=user)
    context = {"user":user,"userprofile":userprofile }
    return render(request , "users/profile.html",context)
