from django.urls import path
from . import views 

#urlcof
urlpatterns = [
    path('', views.home_page, name="home"),
    path('aboutus/',views.about_us, name="aboutus"),
    path('support/',views.support, name="support"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path('blog/',views.blog_page, name="blog"),
    path('<slug:slug>/',views.article_detail ,name="article_detail"),

]

