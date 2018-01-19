from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_site
from django.contrib.auth import login as loginto_site
from django.contrib.auth.models import User, Permission
from django.http import Http404
from .forms import LoginForm, SignupForm
from info.models import Info
from .models import RegisterAuth

def admin_panel(request):
    if not request.user.is_authenticated:
        raise Http404

    info = Info.objects.order_by('site_name')[0]

    context = {
        'info': info,
        'user_logged_in': True,
    }
    return render(request, 'admin/admin_panel.html', context)

# login page
def login(request):
    # If the user is logged in, redirect to main page
    if request.user.is_authenticated:
        return redirect('admin:admin-panel')

    # If the request is a post, try to log them in
    if request.method == "POST":
        form = LoginForm(request.POST)

        # If the form is not valid, return it with errors
        if not form.is_valid():
            context = { 'form' : form, }
            return render(request, 'admin/login.html', context)

        # Authenticate the user
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        
        # If authenticated, redirect to the homepage
        if user is not None:
            loginto_site(request, user)
            return redirect('admin:admin-panel')

        # Otherwise render the form with errors
        form.add_error(None, 'The username or password is invalid')
        context = { 'form' : form, }
        return render(request, 'admin/login.html', context)        

    # Otherwise render the page
    form = LoginForm()
    context = { 'form' : form, }
    return render(request, 'admin/login.html', context)

def signup(request):
    # If the user is logged in, redirect to main page
    if request.user.is_authenticated:
        return redirect('admin:admin-panel')

    if request.method == "POST":
        form = SignupForm(request.POST)

        # Ensures that the signup form is valid
        if not form.is_valid():
            context = { 'form': form, }
            return render(request, 'admin/signup.html', context)

        # Ensures that the user is authorized to make an account.
        try:
            register_auth = RegisterAuth.objects.get(email=form.cleaned_data["email"])
        except:
            form.add_error("email", "Email not authorized.")
            context = { 'form': form }
            return render(request, 'admin/signup.html', context)

        # Makes new user
        user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        # Adds appropriate permissions to the user
        if register_auth.comic_add:
            user.user_permissions.add(Permission.objects.get(codename="add_comic"))

        if register_auth.comic_change:
            user.user_permissions.add(Permission.objects.get(codename="change_comic"))

        if register_auth.comic_delete:
            user.user_permissions.add(Permission.objects.get(codename="delete_comic"))

        if register_auth.post_add:
            user.user_permissions.add(Permission.objects.get(codename="add_post"))

        if register_auth.post_change:
            user.user_permissions.add(Permission.objects.get(codename="change_post"))

        if register_auth.post_delete:
            user.user_permissions.add(Permission.objects.get(codename="delete_post"))

        if register_auth.user_add:
            user.user_permissions.add(Permission.objects.get(codename="add_user"))

        if register_auth.user_change:
            user.user_permissions.add(Permission.objects.get(codename="change_user"))

        if register_auth.user_delete:
            user.user_permissions.add(Permission.objects.get(codename="delete_user"))

        if register_auth.info_change:
            user.user_permissions.add(Permission.objects.get(codename="change_info"))

        loginto_site(request, user)

        return redirect('admin:admin-panel')

    form = SignupForm()
    context = { 'form': form }
    return render(request, 'admin/signup.html', context)

# logout page
def logout(request):
    logout_site(request)
    return redirect('comic:index')