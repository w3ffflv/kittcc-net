from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import TemplateView






def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is None:
            login(request, user )
            return HttpResponseRedirect('home/')
        else:           
            return HttpResponseRedirect('')
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))
    
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))
    

