from django.http import HttpResponse
from django.shortcuts import render


def check(request):
    return HttpResponse('My profile app, Server successfully connected')