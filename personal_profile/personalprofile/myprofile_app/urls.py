from django.contrib import admin
from django.urls import path, include
from .views import check
from .views_sidenav import about, services, experiences, contacts
from .views_topnav import home, extra_curricular, personal_statement, contact
urlpatterns = [
    path('check', check, name='check'),
    #SIDENAV
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('experiences', experiences, name='experiences'),
    path('contacts', contacts, name='contacts'),

    #TOPNAV
    path('', home, name='home'),
    path('extra_curricular', extra_curricular, name='extra_curricular'),
    path('personal_statement', personal_statement, name='personal_statement'),
    path('contact', contact, name='contact'),

]
