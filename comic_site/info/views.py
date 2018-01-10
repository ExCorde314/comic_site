from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Info, Info404, Info500
from .forms import LoginForm

# login page
def login_page(request):
    # If the user is logged in, redirect to main page
    if request.user.is_authenticated:
        return redirect('comic:index')

    # If the request is a post, try to log them in
    if request.method == "POST":
        form = LoginForm(request.POST)

        # If the form is not valid, return it with errors
        if not form.is_valid():
            context = { 'form' : form, }
            return render(request, 'info/login.html', context)

        # Authenticate the user
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        
        # If authenticated, redirect to the homepage
        if user is not None:
            login(request, user)
            return redirect('comic:index')

        # Otherwise render the form with errors
        form.add_error(None, 'The username or password is invalid')
        context = { 'form' : form, }
        return render(request, 'info/login.html', context)        

    # Otherwise render the page
    form = LoginForm()
    context = { 'form' : form, }
    return render(request, 'info/login.html', context)

# logout page
def logout_page(request):
    logout(request)
    return redirect('comic:index')

# 404 error page
def custom_404(request):
    info = Info.load()
    info404 = Info404.load()

    context = {
        'info': info,
        'info404': info404,
    }

    return render(request, 'info/404_page.html', context)

# 500 error page
def custom_500(request):
    info = Info.load()
    info404 = Info404.load()

    context = {
        'info': info,
        'info500': info500,
    }

    return render(request, 'info/500_page.html', context)

# 403 error page
def custom_403(request):
    info = Info.load()
    info403 = Info403.load()

    context = {
        'info': info,
        'info403': info403,
    }

    return render(request, 'info/403_page.html', context)

# 400 error page
def custom_400(request):
    info = Info.load()
    info400 = Info400.load()

    context = {
        'info': info,
        'info400': info400,
    }

    return render(request, 'info/400_page.html', context)
