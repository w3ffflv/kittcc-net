from MySQLdb import _mysql
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import loader
from school.models import Lietotaji


def logout(request):
    return render(request,"home.html")

def register(request):
    if request.method == "POST":
        lietotaji = Lietotaji()

        lietotaji.username = request.POST['username']
        lietotaji.password = request.POST['password']
        lietotaji.repassword = request.POST['password']
        lietotaji.skola = request.POST['skola']
        lietotaji.skolenuskaits = request.POST['usskolenuskaitsername']
        lietotaji.novads = request.POST['novads']
        if lietotaji.password != lietotaji.repassword:
            return HttpResponseRedirect(template.render({}, request))
        elif lietotaji.username == "" or lietotaji.password == "":
            messages.info(request,'Lietotāja vārds vai parole nevar būt tukšas')
            return  HttpResponseRedirect(template.render({}, request))
        else:
            lietotaji.save()    
    template = loader.get_template('accounts/register.html')
    return HttpResponse(template.render({}, request))

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


