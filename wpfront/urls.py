from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.wp_page, name='wp_page'),  # Dynamic slug-based routing
    path('', views.wp_page, {'slug': 'home'}, name='wp_home'),  # Default to 'home'
]