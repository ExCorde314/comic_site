from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.75

    def items(self):
        return ['blog:index', 'comic:index']

    def location(self, obj):
        return reverse(obj)