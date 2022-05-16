from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin






def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))
    
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))


    

