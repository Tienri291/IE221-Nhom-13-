from typing import Generic
from django.shortcuts import redirect, render
from django.http import HttpResponse, request, response
from django.template import context
from django.views.generic import ListView

from CherryBeauty.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .form import CreateUserForm
from django.contrib import messages
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def support(request):
    return render(request,'support.html')

def register(request):
    form = CreateUserForm(request.POST)

    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Tài khoản đã được tạo với tên đăng nhập: ' + user)

        return redirect('login')

    context = {'form':form}
    return render(request,'register.html',context)

def log_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')


    context = {}
    return render(request,'log_in.html',context) 

def logoutUser(request):
    logout(request)
    return redirect('login')

def blog_page(request):
    p = Paginator(Post.objects.all(),5)
    page = request.GET.get('page')
    posts = p.get_page(page)

    posts_list = Post.objects.all()
    return render(request, 'blog.html', {'posts_list': posts_list , 'posts': posts})

def article_detail(request,slug):
    article = Post.objects.get(slug = slug)
    return render(request, 'article_detail.html', {'post':article}) 


#@login_required(login_url="login")