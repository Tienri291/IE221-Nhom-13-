from dataclasses import field
from django.urls import reverse, reverse_lazy
from django.forms import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request, response
from django.template import context
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .form import CommentForm, CreateUserForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
import json
# Create your views here.
def base(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']
    
    return render(request, 'base.html',{'cartItems':cartItems}) 

def home_page(request):
    makeup_list = Product.objects.filter(collection = 1)
    skincare_list = Product.objects.filter(collection = 2)
    post_list = Post.objects.all()
    brand_list = Brand.objects.all().order_by('-id')

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    return render(request, 'home.html',
    {
        'makeup_list': makeup_list,
        'skincare_list':skincare_list,
        'post_list': post_list,
        'brand_list':brand_list,
        'cartItems':cartItems 
    })

def about_us(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    return render(request, 'about_us.html',{'cartItems':cartItems})


def support(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    return render(request,'support.html',{'cartItems':cartItems})

def brand(request):
    brand_list = Brand.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    return render(request,'brand.html',{
        'brand_list': brand_list,
        'cartItems':cartItems
        })

def register(request):
    form = CreateUserForm(request.POST)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']


    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Tài khoản đã được tạo với tên đăng nhập: ' + user)

        return redirect('login')

    context = {'form':form,'cartItems':cartItems}
    return render(request,'register.html',context)

def log_in(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')


    context = {'cartItems':cartItems}
    return render(request,'log_in.html',context) 

def logoutUser(request):
    logout(request)
    return redirect('login')

def blog_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    p = Paginator(Post.objects.all(),5)
    page = request.GET.get('page')
    posts = p.get_page(page)

    posts_list = Post.objects.all()
    return render(request, 'blog.html', {'posts_list': posts_list , 'posts': posts, 'cartItems':cartItems})

def article_detail(request,slug):
    article = Post.objects.get(slug = slug)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    user = request.user
    return render(request, 'article_detail.html', {'post':article,'cartItems':cartItems,'user':user}) 



def product_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    makeup_list = Product.objects.filter(collection = 1)
    skincare_list = Product.objects.filter(collection = 2)
    return render(request,'product.html',{'makeup_list': makeup_list,'skincare_list': skincare_list,'cartItems':cartItems})

def item_detail(request,item_slug):
    item = Product.objects.get(slug = item_slug)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']


    return render(request,'item_detail.html',{'item':item,'cartItems':cartItems})

def makeuppage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    p = Paginator(Product.objects.filter(collection = 1),12)
    page = request.GET.get('page')
    makeups = p.get_page(page)

    makeup_list = Product.objects.filter(collection = 1)
    brands = Product.objects.distinct().values('brand__title')
    nations = Product.objects.distinct().values('nation__title')
    tags = Product.objects.distinct().values('tag__title')
    return render(request, 'makeup_list.html', 
    {   'makeup_list': makeup_list , 
        'makeups': makeups,    
        'brands': brands,
        'nations': nations,
        'tags': tags,
        'cartItems':cartItems
    })

def skincarepage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    p = Paginator(Product.objects.filter(collection = 2),12)
    page = request.GET.get('page')
    makeups = p.get_page(page)

    makeup_list = Product.objects.filter(collection = 2)
    brands = Product.objects.distinct().values('brand__title','brand__id')
    nations = Product.objects.distinct().values('nation__title','nation__id')
    return render(request, 'skincare_list.html', 
    {   'makeup_list': makeup_list , 
        'makeups': makeups,    
        'brands': brands,
        'nations': nations,
        'cartItems':cartItems
    })


def searchpage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    q = request.GET['q']
    productdata = Product.objects.filter(title__icontains = q).order_by('-id')
    blogdata = Post.objects.filter(title__icontains = q).order_by('-id')
    return render(request,'search.html',{'productdata' : productdata, 'blogdata': blogdata, 'cartItems':cartItems})

@login_required(login_url="login")
def cartpage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']
    
    return render(request, 'cart.html',{'items':items,'order':order,'cartItems':cartItems})


def checkoutpage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.oderitem_set.all()
        cartItems = order.get_cart_items
        

    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems= order['get_cart_items']

    
     
    return render(request,'checkout.html',{'customer':customer,'items':items,'order':order, 'cartItems':cartItems})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('ProductId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem,created = OderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantily = (orderItem.quantily + 1)
    elif action == 'remove':
        orderItem.quantily = (orderItem.quantily - 1) 

    orderItem.save()

    if orderItem.quantily <= 0:
        orderItem.delete() 

    return JsonResponse('Item was added',safe=False)

#def LikeView(request,slug):
#    post = get_object_or_404(Post, id = request.POST.get('post_id'))
#    liked = False
#    if post.likes.filter(id=request.user.id).exists():
#        post.likes.remove(request.user)
#        liked = False
#    else:
#        post.likes.add(request.user)
#        liked = True

#    post.likes.add(request.user)

#    return HttpResponseRedirect(reverse('article_detail',args= [str(slug)]))

def LikeView(request,slug):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)

        else:
           post_obj.likes.add(user) 

        like ,created = Like.objects.get_or_create(user=user, post_id = post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            
            else:
                like.value = 'Like'
        like.save()
    return HttpResponseRedirect(reverse('article_detail',args= [str(slug)]))

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def form_invalid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_invalid(form)
    #fields = '__all__'
    success_url = reverse_lazy('home')

#@login_required(login_url="login")