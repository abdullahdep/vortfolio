from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    def items(self):
        return ['index', 'about', 'projects', 'services', 'contact', 'portfolio', 'learn', 'learning_sd', 'roadmap']
    def location(self, item):
        return reverse(item)
    