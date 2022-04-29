from django.urls import path
from . import views 

#urlcof
urlpatterns = [
    path('', views.home_page),

]
