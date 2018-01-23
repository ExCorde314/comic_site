from django import forms
from .models import About, Info

class AboutEdit(forms.ModelForm):
    class Meta:
        model = About
        exclude = []

class InfoEdit(forms.ModelForm):
    class Meta:
        model = Info
        exclude = ["logo"]