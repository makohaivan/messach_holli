from django.urls import path
from . import views
from .views import contact_form

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', contact_form, name='contact_form'),
    path('services/', views.services, name='services')
]