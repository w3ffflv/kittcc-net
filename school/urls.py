from django.urls import path,include
from school import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', views.login, name="login"),
     path('home/', views.home, name="home"),
     path('signup/', views.signup, name="signup"),
     
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)