"""sichtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Social
from django.contrib.auth import views as auth_views

app_name= 'DynamoDiviaky'
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
#    path('logout/',views.logout_view, name='logout'),
#    path('login/',views.login_user, name='login'),
    path('rezervacie/', views.rez_list, name='rez_list'),
    path('rez_detail/<int:rez_id>', views.rez_detail, name='rez_detail'),
    path('create/', views.create_reservation, name='create_reservation'),
#    path('home/',Social.as_view(), name='home'),
#    path('',Social.as_view(), name='home'),
#    path('accounts/google/login/', auth_views.LoginView.as_view(template_name='DynamoDiviaky/login.html'), name='login'),
    path('show_data/', views.show_data, name='show_data'),
    path('edit_data/<int:pk>/', views.edit_data, name='edit_data'),
    path('insert_data/', views.insert_data, name='insert_data'),
]
