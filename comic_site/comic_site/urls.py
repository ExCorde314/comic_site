from django.urls import include, path, reverse
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from comic.sitemaps import ComicSitemap
from blog.sitemaps import BlogSitemap
from .sitemaps import StaticSitemap
from django.conf.urls import handler404, handler500, handler403, handler400
from info.views import about, about_edit, info_edit, custom_404, custom_500, custom_403, custom_400

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

handler404 = custom_404
handler500 = custom_500
handler403 = custom_403
handler400 = custom_400