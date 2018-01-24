from django import forms
from .models import Comic

class AddComic(forms.ModelForm):
    class Meta:
        model = Comic
        exclude = ['date_published']

class ChangeComic(forms.ModelForm):
    class Meta:
        model = Comic
        exclude = ['date_published', 'image']

class DeleteComic(forms.Form):
    pass