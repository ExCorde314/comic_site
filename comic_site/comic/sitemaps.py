from django.contrib.sitemaps import Sitemap
from .models import Comic

class ComicSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Comic.objects.all()