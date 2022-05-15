from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin


def logout(request):
    return render(request,"home.html")

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def profile(request):
    template = loader.get_template('accounts/profile.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))


