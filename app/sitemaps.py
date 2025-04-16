# filepath: /workspaces/vortfolio/app/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ConsultationRequest

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'projects', 'services', 'contact', 'portfolio', 'learn']

    def location(self, item):
        return reverse(item)

class ConsultationRequestSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ConsultationRequest.objects.all()

    def lastmod(self, obj):
        return obj.updated_at