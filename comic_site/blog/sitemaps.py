from django.contrib.sitemaps import Sitemap
from .models import Post

class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Post.objects.all()