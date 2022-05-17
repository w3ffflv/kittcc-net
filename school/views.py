from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from . models import User
from django.views.generic import DetailView, UpdateView


#class SchoolUpdateView(UpdateView):
 #   model = User
  #  template_name = 'details_view.html'

class SchoolDetailView(DetailView):
    model = User
    template_name = 'details_view.html'
    context_object_name = 'schooluser'


def home(request):
    students = User.objects.all()
    novads = User.objects.filter(user=request.user).values()
    context = {'students':students,'novads':novads}
    return render(request,"home.html", context)


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


