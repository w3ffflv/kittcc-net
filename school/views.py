from curses.ascii import HT
from urllib import request
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
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
    if request.method == 'POST':
        pirmdiena = request.POST['pirmdiena']
        otrdiena = request.POST['otrdiena']
        tresdiena = request.POST['tresdiena']
        ceturdiena = request.POST['ceturdiena']
        piekdiena = request.POST['piekdiena']
        print(pirmdiena,otrdiena,tresdiena,ceturdiena,piekdiena)
         
        

    template_name = 'accounts/profile.html'
