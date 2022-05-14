from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.shortcuts import render


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({},request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'
    


def list_posts(request):
    # Limit to 10 latest posts
    posts = Post.objects.all().order_by('-created_at')[:10]

    posts_text = ""

    for post in posts:
        posts_text += f"@{post.created_by} {post.contents}"

    return HttpResponse(posts_text)

def list_posts(request):
    # Limit to 10 latest posts.
    posts = Post.objects.all().order_by('-created_at')[:10]

    return render(request, 'templates/home.html', {'posts': posts})