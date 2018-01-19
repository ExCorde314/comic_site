from django.shortcuts import render
from .models import Info, Info404, Info500, About

# About the comic page.
def about(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info = Info.load()
    about = About.load()

    context = {
        'info': info,
        'about': about,
        'user_logged_in': user_logged_in,
    }

    return render(request, 'info/about.html', context)

# 404 error page
def custom_404(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info = Info.load()
    info404 = Info404.load()

    context = {
        'info': info,
        'info404': info404,
        'user_logged_in': user_logged_in,
    }

    response.status_code = 404

    return render(request, 'info/404_page.html', context)

# 500 error page
def custom_500(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info = Info.load()
    info404 = Info404.load()

    context = {
        'info': info,
        'info500': info500,
        'user_logged_in': user_logged_in,
    }

    response.status_code = 500

    return render(request, 'info/500_page.html', context)

# 403 error page
def custom_403(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info = Info.load()
    info403 = Info403.load()

    context = {
        'info': info,
        'info403': info403,
        'user_logged_in': user_logged_in,
    }

    response.status_code = 403

    return render(request, 'info/403_page.html', context)

# 400 error page
def custom_400(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info = Info.load()
    info400 = Info400.load()

    context = {
        'info': info,
        'info400': info400,
        'user_logged_in': user_logged_in,
    }

    response.status_code = 400

    return render(request, 'info/400_page.html', context)
