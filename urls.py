"""
URL configuration for psicomedic_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# psicomedic/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('psychologists/', views.list_psychologist, name='list_psychologist'),
    path('psychologists/<int:pk>/', views.get_psychologist, name='get_psychologist'),
    path('patients/', views.list_patients, name='list_patients'),
    path('patients/<int:pk>/', views.get_patient, name='get_patient'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/<int:pk>/', views.get_appointment, name='get_appointment'),
]

