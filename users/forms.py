from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField
from .models import Profile
from django.http import  HttpResponseRedirect

class RegistrationForm(UserCreationForm):

    '''custom registration form inherits from UserCreationForm provided by django authentication
        forms . email field exists in the database already'''
        
    email = forms.EmailField(required=True,max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter new password'}),label="password",help_text="at least 8 charachters , numbers , symbols or better mix them")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm your password'}),label="confirm password")
    class Meta:
        model = User
        fields =['username','email','first_name' , 'last_name' ]
        widgets = {
			'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
		}

class ProfileForm(forms.ModelForm):

    '''custom profile form in order to handle the extra fields added to user profile (profile picture)
        will be provided through the form till now .. the other extra fields will be controlled from 
        else where '''

    profile_pic =forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ['profile_pic',]

class LoginForm(AuthenticationForm):          
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True, 'placeholder': 'username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))