from django import forms
from .models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['date_published']

class ChangePost(forms.ModelForm):    
    class Meta:
        model = Post
        exclude = ['date_published']

class DeletePost(forms.Form):
    pass