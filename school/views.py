from curses.ascii import HT
from urllib import request
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    template = loader.get_template('home.html')
    School=School.objects.all()
    if request.method == ['POST']:
        username = request.POST['username']
        password = request.POST['password']
        skola = request.POST['skola']
        novads = request.POST['novads']
        skolenuskaits = request.POST['skolenuskaits']
        apestas_porcijas = request.POST['apestas_porcijas']
        pirmdiena = request.POST['pirmdiena']
        otrdiena = request.POST['otrdiena']
        tresdiena = request.POST['tresdiena']
        ceturdiena = request.POST['ceturdiena']
        piekdiena = request.POST['piekdiena']
        obj = School()
        obj.username = username
        obj.password = password
        obj.skola = skola
        obj.novads = novads
        obj.skolenuskaits = skolenuskaits
        obj.apestas_porcijas = apestas_porcijas
        obj.pirmdiena = pirmdiena
        obj.otrdiena = otrdiena
        obj.tresdiena = tresdiena
        obj.ceturdiena = ceturdiena
        obj.piekdiena = piekdiena
        obj.save()

        from django.core import serializers

        data = serializers.serialize("python",School.objects.all())
        context = {
            'data':data,
        }

    return HttpResponse(template.render({},request),context)

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
    
         
        

   
