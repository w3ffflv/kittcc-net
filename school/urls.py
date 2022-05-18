from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ 
     path('', auth_views.LoginView.as_view(template_name = "login.html"), name="login"),
     path('accounts/logout', auth_views.LogoutView.as_view(), name="logout"),
     path('about/', views.about, name="about"),
     path('contact/', views.contact, name="contact"),
     path('accounts/profile/', views.ProfileView.as_view(), name="profile"),
     path('home/', views.home, name="home"),  
     path('user/<int:pk>', views.SchoolDetailView.as_view(), name="school-detail"),
     path('update/<int:pk>',views.SchoolUpdateView.as_view(), name='school-update'),
     path('search/',views.SchoolSeacrhListView.as_view(), name="school-search")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)