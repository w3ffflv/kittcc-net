from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from school.models import Lietotaji
import mysql as sql
un=''
pwd=''

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
    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="192.236.178.44",user="othbpjti_skola2022",passwd="s[Qe6mG]v6TR",database='othbpjti_skola')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                un=value
            if key=="password":
                pwd=value
        
        c="select * from lietotaji where username='{}' and password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'')

        
    

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


