# ex01/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.django_page, name='ex01_django'),
    path('display/', views.display_page, name='ex01_display'),
    path('templates/', views.template_page, name='ex01_templates'),
]
