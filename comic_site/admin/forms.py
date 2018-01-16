from django import forms

# The form for logging into the admin
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()