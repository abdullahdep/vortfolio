from django.urls import path, include
from . import views

urlpatterns = [
    path('wp/', include('wpfront.urls')),  # Make sure this is included
    path('<str:slug>/', views.wp_page, name='wp_page'),
    path('', views.wp_page, name='wp_home'),
]
