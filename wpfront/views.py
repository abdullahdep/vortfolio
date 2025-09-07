from django.shortcuts import render
from django.http import Http404
from .models import Page

def wp_page(request, slug='home'):
    try:
        page = Page.objects.get(slug=slug)
        return render(request, "wpfront/page.html", {
            "content": page.content,
            "title": page.title
        })
    except Page.DoesNotExist:
        return render(request, "404.html", status=404)
