from django.http import HttpResponse
from django.shortcuts import render

# HOME
def home(request):
    context = {}
    return render(request, "main_pages/topnav/01home.html", context)

def extra_curricular(request):
    context = {}
    return render(request, "main_pages/topnav/02extra_curricular.html", context)


def personal_statement(request):
    context = {}
    return render(request, "main_pages/topnav/03personal_statement.html", context)


def get_in_touch(request):
    context = {}
    return render(request, "main_pages/topnav/04get_in_touch.html", context)


