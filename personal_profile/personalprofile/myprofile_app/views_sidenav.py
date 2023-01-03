from django.http import HttpResponse
from django.shortcuts import render

# HOME
def about(request):
    context = {}
    return render(request, "main_pages/sidenav/01about.html", context)

def services(request):
    context = {}
    return render(request, "main_pages/sidenav/02services.html", context)

def experiences(request):
    context = {}
    return render(request, "main_pages/sidenav/03experiences.html", context)

def contacts(request):
    context = {}
    return render(request, "main_pages/sidenav/04contact.html", context)

