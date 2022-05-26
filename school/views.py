from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from . models import User
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import UserForm



class SchoolUpdateView(UpdateView):
    model = User
    template_name = 'update_school_info.html'
    context_object_name = 'schooluser'
    form_class = UserForm

class SchoolUpdateSettingsView(UpdateView):
    model = User
    template_name = 'update_school_settings.html'
    context_object_name = 'schooluser'
    form_class = UserForm

class SchoolDetailView(DetailView):
    model = User
    template_name = 'details_view.html'
    context_object_name = 'schooluser'

@login_required
def home(request):

    students = User.objects.all() 
    return render(request,"skolas.html", {'students':students})


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))
 

def create(request):
    error=''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error='Forma bija uzrakstīta kļūdaini'
            

    form = UserForm()

    data = {
        'form':form,
        'error':error
    }
    template = loader.get_template('update_school_info.html')
    return HttpResponse(template.render({}, request),data)
   
@login_required
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))
@login_required
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))



class ProfileView(LoginRequiredMixin,TemplateView):
    context_object_name = 'schooluser'
    template_name = 'accounts/profile.html'

def schoolsearch(request):

    students = User.objects.all() 
    
    if 'q' in request.GET:
        q = request.GET['q']
        students = User.objects.filter(skola__icontains=q)
    else:
        students = User.objects.all()
    return render(request,"skolas.html", {'students':students})

