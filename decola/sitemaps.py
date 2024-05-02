from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post

class PostSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.data_publicacao
