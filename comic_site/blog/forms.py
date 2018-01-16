from django import forms
from .models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['date_published']

class ChangePost(forms.ModelForm):
    title = forms.CharField(max_length=200, required=False)
    author = forms.CharField(max_length=200, required=False)
    alt_text = forms.CharField(max_length=200, required=False)
    
    class Meta:
        model = Post
        exclude = ['date_published']