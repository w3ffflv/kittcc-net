from curses.ascii import HT
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from . models import User
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import UserForm

class SchoolUpdateView(UpdateView):
    model = User
    template_name = 'update_school_info.html'
    
    form_class = UserForm

class SchoolDetailView(DetailView):
    model = User
    template_name = 'details_view.html'
    context_object_name = 'schooluser'

@login_required
def home(request):
    students = User.objects.all() 
    return render(request,"home.html", {'students':students})


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))
 

def create(request):
    error=''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/profile/')
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
    template_name = 'accounts/profile.html'


