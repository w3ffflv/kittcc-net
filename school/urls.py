from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', auth_views.LoginView.as_view(template_name = "index.html"), name="index"),
     path('about/', views.about, name="about"),
     path('contact/', views.contact, name="contact"),
     path('accounts/profile/', views.ProfileView.as_view(), name="profile"),
     path('home/', views.home, name="home"),

     # Django Auth
     path('accounts/login', auth_views.LoginView.as_view(template_name ="accounts/login.html"), name='login'),
     path('accounts/logout', auth_views.LogoutView.as_view(), name="logout")
  
]