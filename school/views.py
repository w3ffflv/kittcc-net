from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin






def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

    

