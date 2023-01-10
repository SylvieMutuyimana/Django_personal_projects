from django.http import HttpResponse
from django.shortcuts import render

# HOME
def home(request):
    context = {}
    return render(request, "home.html", context)

def check(request):
    return HttpResponse('My profile app, Server successfully connected')