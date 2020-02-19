from django.shortcuts import render 
from django.http import  HttpResponseRedirect
from .forms import RegistrationForm , ProfileForm
from posts  import views as post_views
from .models import Profile


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
            print("created")  # for debugging purposes
            return HttpResponseRedirect("/") # redirect to homepage (posts page)
        else:
            print("invalid") # for debugging purposes
            
            
    else:
        user_form = RegistrationForm()
        profile_form = ProfileForm()
    context = {"user_form":user_form,"profile_form":profile_form}
    return render(request , 'users/register.html',context)
