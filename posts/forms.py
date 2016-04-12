from django import forms
from .models import Post

class PostForm(forms.ModelForm):  #argument is a form object
	class Meta:
		model = Post
		fields = [
			"title",
			"content"
			]