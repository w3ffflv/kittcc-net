from curses.ascii import HT
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    if request.method == 'POST':
        pirmdiena = request.POST['pirmdiena']
        otrdiena = request.POST['otrdiena']
        tresdiena = request.POST['tresdiena']
        ceturdiena = request.POST['ceturdiena']
        piekdiena = request.POST['piekdiena']
        print(pirmdiena,otrdiena,tresdiena,ceturdiena,piekdiena)
    return render(request,'home.html')

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))

class ProfileView(LoginRequiredMixin,TemplateView,request):
    template_name = 'accounts/profile.html'

    
    
         
        

   
