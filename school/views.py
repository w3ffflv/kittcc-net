from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student
from django.views.generic.detail import DetailView




def home(request):
    Lietotaji = Student.objects.all()
    return render(request,"home.html",{'Lietotaji':Lietotaji})


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))

class ProfileView(DetailView):
    model = Student()
    context_object_name = 'user_object'
    template_name = 'accounts/profile.html'


class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'
    

