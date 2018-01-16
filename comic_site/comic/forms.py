from django import forms
from .models import Comic

class AddComic(forms.ModelForm):
    class Meta:
        model = Comic
        exclude = ['date_published']

class ChangeComic(forms.ModelForm):
    title = forms.CharField(max_length=200, required=False)
    image = forms.ImageField(required=False)
    title_text = forms.CharField(max_length=200, required=False)
    alt_text = forms.CharField(max_length=200, required=False)
    
    class Meta:
        model = Comic
        exclude = ['date_published']