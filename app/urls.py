from django.urls import path
from . import views

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
]