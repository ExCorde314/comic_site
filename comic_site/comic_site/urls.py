"""comic_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('comic.urls')),
    url(r'^comic/', include('comic.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^access-portal/', include('admin.urls')),
]

handler404 = 'info.views.custom_404'
handler500 = 'info.views.custom_500'
handler403 = 'info.views.custom_403'
handler400 = 'info.views.custom_400'