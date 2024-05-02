from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse
from datetime import datetime

class CustomSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['home', 'helloworld']

    def lastmod(self, obj):
        # Define manualmente a data de modificação para cada URL
        if obj == 'home':
            return datetime(2024, 5, 1)
        elif obj == 'helloworld':
            return datetime(2024, 5, 1)

    def location(self, obj):
        # Gera automaticamente a URL para cada item usando a função reverse()
        return reverse(obj)

class PostSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('blog_detail', args=[obj.slug])
