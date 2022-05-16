from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from school.models import Student





def home(request):
    students = Student.objects.all()
    return render(request,"home.html",{'student':students})


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))




class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'
    

