from django import forms
from .models import Post, Comment

class UserLoginForm(forms.ModelForm):
	class Meta:
		username = forms.CharField(label="")
		password = forms.CharField(label="" ,widget=forms.PasswordInput)







class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'status','restrict_comment',)


			

class PostEditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'status','restrict_comment',)




class CommentForm(forms.ModelForm):
	content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'reply', 'rows':'9', 'cols':'50'}))
	class Meta:
		model = Comment
		fields = ('content',)
			

class CommentEditForm(forms.ModelForm):
	content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'reply', 'rows':'9', 'cols':'50'}))
	class Meta:
		model = Comment
		fields = ('content',)
			

		
		