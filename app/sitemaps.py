# filepath: /workspaces/vortfolio/app/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ConsultationRequest

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['index', 'projects', 'services', 'portfolio', 'learn']

    def location(self, item):
        return reverse(item)
