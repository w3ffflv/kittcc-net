from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),

  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)