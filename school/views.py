from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from school.models import Lietotaji
from django.db.models import Q
from django.contrib.auth.decorators import login_required




def home(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(id__icontains=q) | Q(skola__icontains=q) | Q(skolenuskaits__icontains=q) | Q(novads__icontains=q) | Q(apestasporcijas__icontains=q) | Q(pirmdiena__icontains=q) | Q(otrdiena__icontains=q) | Q(tresdiena__icontains=q) | Q(ceturdiena__icontains=q) | Q(piekdiena__icontains=q) )
        lietotaji = Lietotaji.objects.filter(multiple_q)

    else:
        lietotaji = Lietotaji.objects.all()
    return render(request,"home.html",{'lietotaji':lietotaji})

@login_required(login_url='login.html')
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
    

