from django.shortcuts import render
from .models import Info, Info404, Info500

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