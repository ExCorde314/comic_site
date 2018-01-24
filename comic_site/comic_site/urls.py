from django.urls import include, path, reverse
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from comic.sitemaps import ComicSitemap
from blog.sitemaps import BlogSitemap
from .sitemaps import StaticSitemap
from info.views import about, about_edit, info_edit

sitemaps = {
    'static': StaticSitemap(),
    'comic': ComicSitemap(),
    'blog': BlogSitemap(),
}

urlpatterns = [
    path('', include('comic.urls')),
    path('about', about, name="about"),
    path('about/edit', about_edit, name="about-edit"),
    path('info/edit', info_edit, name="info-edit"),
    path('blog/', include('blog.urls')),
    path('access-portal/', include('admin.urls')),
    path('robots.txt', lambda r: HttpResponse('Sitemap: ' + reverse('django.contrib.sitemaps.views.sitemap') + "\nUser-Agent: *\nDisallow:", content_type="text/plain"), name="robots_txt"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'info.views.custom_404'
handler500 = 'info.views.custom_500'
handler403 = 'info.views.custom_403'
handler400 = 'info.views.custom_400'