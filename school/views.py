from curses.ascii import HT
from urllib import request
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Details


def home(request):
     template = loader.get_template('home.html')
     if request.method == 'POST':
        skola = request.POST['skola']
        skolenuskaits = request.POST['skolenuskaits']
        #Creating the Object of record every time user clicks on 'Add Data'
        obj = Details()
        obj.skola = skola
        obj.skolenuskaits = skolenuskaits
        obj.save()
        
    #Fetching the details and saving in an dictionary
        from django.core import serializers
        data = serializers.serialize("python",Details.objects.all());

    #Dictionary to store the data and send it back to HTML format
        context = {
            'data':data,
        }
        return HttpResponse(template.render({},request))

@login_required()
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