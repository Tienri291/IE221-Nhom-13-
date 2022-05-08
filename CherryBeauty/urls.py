from django.urls import path
from . import views 

#urlcof
urlpatterns = [
    path('', views.home_page, name="home"),
    path('search/',views.searchpage, name ="search"),
    path('aboutus/',views.about_us, name="aboutus"),
    path('support/',views.support, name="support"),
    path('register/',views.register, name="register"),
    path('login/',views.log_in, name="login"),
    path('logout/',views.logoutUser, name = "logout"),
    path('blog/',views.blog_page, name="blog"),
    path('product/',views.product_page, name ="product"),
    path('makeup/',views.makeuppage, name ="makeup"),
    path('skincare/',views.skincarepage, name ="skincare"),  
    path('brand/',views.brand,name="brand"),
    path('<slug:slug>/',views.item_detail,name="item_detail"),
    path('<slug:slug>/',views.article_detail ,name="article_detail"),

]

