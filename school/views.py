from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout







def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is None:
            login(request, user )
            template = loader.get_template('home.html')
            return HttpResponseRedirect(template.render({}, request))
        else:           
            template = loader.get_template('login.html')
            return HttpResponseRedirect(template.render({}, request))
    
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))


    

