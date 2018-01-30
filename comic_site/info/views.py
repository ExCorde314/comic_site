from django.shortcuts import render, redirect
from .models import Info, Info404, Info500, About
from .forms import AboutEdit, InfoEdit
from django.http import Http404

# About the comic page.
def about(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    about = About.load()

    context = {
        'about': about,
        'user_logged_in': user_logged_in,
    }

    return render(request, 'info/about.html', context)

def about_edit(request):
    if not request.user.is_authenticated or not request.user.has_perm('info.change_info'):
        raise Http404

    about = About.load()

    if request.method == "POST":
        form = AboutEdit(request.POST, instance=about)

        if not form.is_valid():
            context = {
                'about': about,
                'user_logged_in': True,
                'form': form,
            }

            return render(request, 'info/about_edit.html', context)

        form.save()
        return redirect("about")

    form = AboutEdit(instance=about)

    context = {
        'about': about,
        'user_logged_in': True,
        'form': form,
    }

    return render(request, 'info/about_edit.html', context)

def info_edit(request):
    if not request.user.is_authenticated or not request.user.has_perm('info.change_info'):
        raise Http404

    info = Info.load()

    if request.method == "POST":
        form = InfoEdit(request.POST, instance=info)

        if not form.is_valid():
            context = {
                'user_logged_in': True,
                'form': form,
            }

            return render(request, 'info/info_edit.html', context)

        form.save()
        return redirect("admin:admin-panel")

    form = InfoEdit(instance=info)

    context = {
        'user_logged_in': True,
        'form': form,
    }

    return render(request, 'info/info_edit.html', context)

# 404 error page
def custom_404(request, exception):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info404 = Info404.load()

    context = {
        'info404': info404,
        'user_logged_in': user_logged_in,
    }

    return render(request, 'info/404_page.html', context, status=404)

# 500 error page
def custom_500(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info500 = Info500.load()

    context = {
        'info500': info500,
        'user_logged_in': user_logged_in,
    }

    return render(request, 'info/500_page.html', context, status=500)

# 403 error page
def custom_403(request, exception):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info403 = Info403.load()

    context = {
        'info403': info403,
        'user_logged_in': user_logged_in,
    }

    return render(request, 'info/403_page.html', context, status=403)

# 400 error page
def custom_400(request, exception):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    info400 = Info400.load()

    context = {
        'info400': info400,
        'user_logged_in': user_logged_in,
    }

    return render(request, 'info/400_page.html', context, status=400)
