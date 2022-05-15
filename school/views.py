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
    con = _mysql.connect(host='192.236.178.44',user='othbpjti_skola2022',database='othbpjti_skola',password='s[Qe6mG]v6TR')
    cursor = con.cursor()
    sqlusername = "select username from school_lietotaji"
    sqlpassword = "select password from school_lietotaji" 
    cursor.execute(sqlusername,sqlpassword)
    u=[]
    p=[]
    for i in cursor:
        u.append(i)
    for j in cursor:
        p.append(j)
        res = list(map(itemgetter(0),u))
        res2 = list(map(itemgetter(0),p))
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            i=1
            k=len(res)
            while i < k:
                if res[i]==username and res[i] == password:
                    return HttpResponse(render,'welcome.html',{'username':username})
                    break
                i+=1
            else:
                messages.info(request,"Parbaudiet Vardu vai paroli")    
        
       
    return HttpResponse(template.render({}, request))
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


