from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.login, name="login"),
     path('accounts/logout', views.logout, name="logout"),
     path('about/', views.about, name="about"),
     path('contact/', views.contact, name="contact"),
     path('accounts/profile/', views.profile, name="profile"),
     path('home/', views.home, name="home"),
     path('accounts/register',views.register,name="register"),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)