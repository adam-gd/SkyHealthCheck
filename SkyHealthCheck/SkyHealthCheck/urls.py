"""
URL configuration for SkyHealthCheck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from myapp import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), 
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', include('myapp.urls')),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),
]
