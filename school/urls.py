from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import list_posts


urlpatterns = [
     path('', auth_views.LoginView.as_view(template_name = "index.html"), name="index"),
     path('accounts/logout', auth_views.LogoutView.as_view(), name="logout"),
     path('about/', views.about, name="about"),
     path('contact/', views.contact, name="contact"),
     path('accounts/profile/', views.ProfileView.as_view(), name="profile"),
     path('home/', list_posts),
     
    

     # Django Auth
     path('accounts/login', auth_views.LoginView.as_view(template_name ="index.html"), name='login'),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)