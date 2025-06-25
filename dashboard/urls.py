from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.custom_login, name='login'),  
    path('logout/', views.custom_logout, name='logout'),

    path('addFaq/', views.addFaq, name='addFaq'),
    path('updateFaq/<int:pk>/', views.updateFaq, name='updateFaq'),
    path('deleteFaq/<int:pk>/', views.deleteFaq, name='deleteFaq'),

    path('addTestimonial/', views.addTestimonial, name='addTestimonial'),
    path('editTestimonial/<int:pk>/', views.updateTestimonial, name='editTestimonial'),
    path('deleteTestimonial/<int:pk>/', views.deleteTestimonial, name='deleteTestimonial'),

    path('addPhoto/', views.addPhoto, name='photo'),
    path('addSkill/', views.addSkill, name='addSkill'),
]