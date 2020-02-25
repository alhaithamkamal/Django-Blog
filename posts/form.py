from django import forms 
from posts.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=('title','body','image','status', 'category')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control-file'}),
			'status': forms.Select(attrs={'class': 'custom-select'}),
			'category': forms.Select(attrs={'class': 'custom-select'}),
		}