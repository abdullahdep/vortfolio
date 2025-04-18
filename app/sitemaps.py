# filepath: /workspaces/vortfolio/app/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse, get_resolver

class DynamicSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        # Dynamically fetch all named URLs
        url_names = [
            name for name in get_resolver().reverse_dict.keys()
            if isinstance(name, str)  # Ensure it's a named URL
        ]
        return url_names

    def location(self, item):
        return reverse(item)
