from django.urls import path
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import DynamicSitemap
from . import views

sitemaps = {
    'dynamic': DynamicSitemap,
}

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path('portfolio', views.portfolio, name='portfolio'),
    path('learn', views.learn, name='learn'),
    path('learning_sd', views.learning_sd , name='learning_sd'),
    path('roadmap', views.roadmap, name='roadmap'),
    path('consultation/<int:id>/', views.consultation_detail, name='consultation_detail'),
    path('bca6356bcc6f4e32986944a2297de9e7.txt', views.serve_txt_file, name='serve_txt_file'),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('sitemap_index.xml', views.dynamic_sitemap, name='dynamic_sitemap'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('html', views.html, name='html'),
]