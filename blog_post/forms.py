from django import forms
from .models import BlogPost
class AddForm(forms.ModelForm):
	#title = forms.CharField(max_length = 20)
	#post = forms.CharField()
	#user = forms.CharField(max_length = 20)
	class Meta:
		model = BlogPost
		fields = ['title', 'post', 'user',]
