from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from school.models import Student,models





def home(request):
    students = Student.objects.all()
    return render(request,"home.html",{'student':students})


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))

def login(request):
    if request.method == 'POST':
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        skola = models.CharField(max_length=100)
        novads = models.CharField(max_length=100)
        skolenuskaits = models.CharField(max_length=100)
        apestasporcijas = models.CharField(max_length=100)
    return render(request,'index.html')

    

