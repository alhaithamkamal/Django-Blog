from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=('title','body','image','status', 'category', 'restrict_comment')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control-file'}),
			'status': forms.Select(attrs={'class': 'custom-select'}),
			'category': forms.Select(attrs={'class': 'custom-select'}),
		}


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