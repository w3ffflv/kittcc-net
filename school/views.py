from operator import itemgetter
from MySQLdb import _mysql
from django import template
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
        lietotaji.repassword = request.POST['repassword']
        lietotaji.skola = request.POST['skola']
        lietotaji.skolenuskaits = request.POST['skolenuskaits']
        lietotaji.novads = request.POST['novads']

        lietotaji.save()    
    template = loader.get_template('accounts/register.html')
    return HttpResponse(template.render({}, request))

def login(request):

    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def home(request):
    lietotaji = Lietotaji.objects.all()
    return render(request,"home.html",{'lietotaji':lietotaji}) 

def profile(request):
    
    template = loader.get_template('accounts/profile.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))


