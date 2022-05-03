from django.shortcuts import redirect, render
from django.http import HttpResponse, request, response
from django.views.generic import ListView

from CherryBeauty.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views import View

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def support(request):
    return render(request,'support.html')

def login(request):
    return render(request,'log_in.html')

def register(request):
    return render(request,'register.html')

def blog_page(request):
    p = Paginator(Post.objects.all(),5)
    page = request.GET.get('page')
    posts = p.get_page(page)

    posts_list = Post.objects.all()
    return render(request, 'blog.html', {'posts_list': posts_list , 'posts': posts})

def article_detail(request,slug):
    article = Post.objects.get(slug = slug)
    return render(request, 'article_detail.html', {'post':article}) 
