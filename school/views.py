from tkinter import Scrollbar
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from school.models import School


def home(request):
    skola = School.objects.all()
    context = {
        'data': skola
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render({},request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))

class ProfileView(LoginRequiredMixin,TemplateView):
    
    template_name = 'accounts/profile.html'
    

