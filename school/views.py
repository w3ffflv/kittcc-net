from django import template
from django.http import HttpResponse, HttpResponseRedirect
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Lietotaji.empAuth_objects.get(username=username,password=password)
            if user is not None:
                return HttpResponseRedirect(request, 'home.html', {})
            else:
                print("Someone tried to login and faield")
                print("They  used username: {} and password: {}".format(username,password))

                return HttpResponseRedirect('')
        except Exception as identifeir:

            return HttpResponseRedirect('')

    else:
        template = loader.get_template('home.html')
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


