from django.contrib import admin
from django.urls import path, include

from template_app1 import views

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    path('', views.home, name='home'),
]
