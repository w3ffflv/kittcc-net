from curses.ascii import HT
from email import message
import MySQLdb
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from operator import itemgetter
import mysql
from school.models import Lietotaji


def logout(request):
    return render(request,"home.html")

def register(request):
    con = mysql.connect(host="192.236.178.44",user="othbpjti_skola2022",password="s[Qe6mG]v6TR",database="othbpjti_skola")
    if request.method == "POST":
        lietotaji = Lietotaji()

        lietotaji.username = request.POST['username']
        lietotaji.password = request.POST['password']
        lietotaji.repassword = request.POST['password']
        lietotaji.skola = request.POST['skola']
        lietotaji.skolenuskaits = request.POST['usskolenuskaitsername']
        lietotaji.novads = request.POST['novads']
        lietotaji.apestasporcijas = request.POST['apestasporcijas']
        lietotaji.pirmdiena = request.POST['pirmdiena']
        lietotaji.otrdiena = request.POST['otrdiena']
        lietotaji.tresdiena = request.POST['tresdiena'] 
        lietotaji.ceturdiena = request.POST['ceturdiena']
        lietotaji.piekdiena = request.POST['piekdiena']
        if lietotaji.password != lietotaji.repassword:
            return redirect('accounts/register')
        elif lietotaji.username == "" or lietotaji.password == "":
            messages.info(request,'Lietotāja vārds vai parole nevar būt tukšas')
            return redirect('accounts/register')
        else:
            lietotaji.save()    
    template = loader.get_template('accounts/register.html')
    return HttpResponse(template.render({}, request))

def login(request):
    con = MySQLdb.connect(host="192.236.178.44",user="othbpjti_skola2022",password="s[Qe6mG]v6TR",database="othbpjti_skola")
    cursor = con.cursor()
    username = "select username from school_lietotaji"
    password = "select password from school_lietotaji"
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


