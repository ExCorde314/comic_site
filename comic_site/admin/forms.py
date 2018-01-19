from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# The form for logging into the admin
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class SignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean(self):
        form_data = self.cleaned_data

        try:
            if form_data['password1'] != form_data['password2']:
                self.add_error("password1", "Passwords do not match.")
                self.add_error("password2", "Passwords do not match.")
        except KeyError:
            pass

        return form_data