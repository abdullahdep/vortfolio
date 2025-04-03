from django.shortcuts import render

# Create your views here.

siteName = "Vortfolio"

siteName= {"siteName": siteName}


def index(request):
    return render(request, "index.html" ,siteName)
def about(request):
    return render(request, "about.html" ,  siteName)
def projects(request):
    return render(request, "projects.html", siteName)
def services(request):
    return render(request, "services.html", siteName)
def contact(request):
    return render(request, "contact.html", siteName)
def portfolio(request):
    return render(request, "portfolio.html", siteName)
