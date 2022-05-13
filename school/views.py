from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))


@login_required()
def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render({}, request))