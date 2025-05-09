"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls import handler404
from app import views  # Import the custom 404 view from the app
# from app.sitemaps import StaticViewSitemap
from app.views import  ads_txt ,privacy_policy

handler404 = views.custom_404_view

# sitemaps = {
#     'static': StaticViewSitemap}

from django.contrib.sitemaps.views import sitemap


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('auth_app.urls')),
    # path('robots.txt', robots_txt, name='robots_txt'),
    path("ads.txt", ads_txt, name="ads_txt"),
    path('privacy-policy', privacy_policy, name='privacy_policy'),
    path('pages/', include('wpfront.urls')),
    path('accounts/', include('allauth.urls')),




]
