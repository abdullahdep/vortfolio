from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path('portfolio', views.portfolio, name='portfolio'),
    path('learn', views.learn, name='learn'),
    path('ads.txt', TemplateView.as_view(
        template_name='ads.txt',
        content_type='text/plain'
    ), name='ads_txt'),
]