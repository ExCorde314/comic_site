from django.urls import include, path
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from comic.sitemaps import ComicSitemap
from blog.sitemaps import BlogSitemap
from .sitemaps import StaticSitemap

sitemaps = {
    'static': StaticSitemap(),
    'comic': ComicSitemap(),
    'blog': BlogSitemap(),
}

urlpatterns = [
    path('', include('comic.urls')),
    path('blog/', include('blog.urls')),
    path('access-portal/', include('admin.urls')),
    path('robots.txt', lambda r: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_txt"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'info.views.custom_404'
handler500 = 'info.views.custom_500'
handler403 = 'info.views.custom_403'
handler400 = 'info.views.custom_400'