from django.urls import path,include
from school import views
from django.conf import settings
from django.conf.urls.static import static
from .views import home, profile, RegisterView



urlpatterns = [
     path('', home, name='users-home'),
     path('register/', RegisterView.as_view(), name='users-register'),
     path('profile/', profile, name='users-profile'),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)