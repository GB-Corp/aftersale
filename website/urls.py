"""pcapiproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views
from .sitemaps import *

app_name = 'website'

router = routers.DefaultRouter()

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    # SiteMap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    # Main pages
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('workshops/', views.workshops, name='workshops'),
    path('register-workshop/', views.register_workshop, name='register_workshop'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/content/', views.dashboard_content, name='dashboard_content'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='website/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='website/auth/password_reset.html',
        email_template_name='website/auth/password_reset_email.html',
        subject_template_name='website/auth/password_reset_subject.txt'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='website/auth/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='website/auth/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='website/auth/password_reset_complete.html'
    ), name='password_reset_complete'),
    
    # User Profile
    path('accounts/profile/', views.profile, name='profile'),
]
