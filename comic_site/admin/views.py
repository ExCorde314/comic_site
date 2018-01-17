from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from .forms import LoginForm
from info.models import Info

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
def login_page(request):
    # If the user is logged in, redirect to main page
    if request.user.is_authenticated:
        return redirect('admin:admin-panel')

    # If the request is a post, try to log them in
    if request.method == "POST":
        form = LoginForm(request.POST)

        # If the form is not valid, return it with errors
        if not form.is_valid():
            context = { 'form' : form, }
            return render(request, 'admin/login_page.html', context)

        # Authenticate the user
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        
        # If authenticated, redirect to the homepage
        if user is not None:
            login(request, user)
            return redirect('admin:admin-panel')

        # Otherwise render the form with errors
        form.add_error(None, 'The username or password is invalid')
        context = { 'form' : form, }
        return render(request, 'admin/login_page.html', context)        

    # Otherwise render the page
    form = LoginForm()
    context = { 'form' : form, }
    return render(request, 'admin/login_page.html', context)

# logout page
def logout_page(request):
    logout(request)
    return redirect('comic:index')