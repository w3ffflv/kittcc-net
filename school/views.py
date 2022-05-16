from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin






def home(request):
    return HttpResponse(request,"home.html")

def login(request):
    return HttpResponse(request,"index.html")

def signup(request):
    return HttpResponse(request,"signup.html")

    

