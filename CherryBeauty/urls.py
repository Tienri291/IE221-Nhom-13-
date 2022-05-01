from django.urls import path
from . import views 

#urlcof
urlpatterns = [
    path('', views.home_page),
    path('aboutus/',views.about_us),
    path('support/',views.support),
    path('blog/',views.blog_page, name="blog"),
    path('<slug:slug>/',views.article_detail ,name="article_detail"),

]

