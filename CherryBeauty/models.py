from ast import mod
from distutils.command.upload import upload
import imp
from lib2to3.refactor import MultiprocessingUnsupported
from turtle import color, title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True, upload_to="images/blog/")
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextUploadingField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    @property
    def headerimageURL(self):
        try:
            url = self.header_image.url
        except:
            url = ''
        return url
 
class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "brand_img/")

    def __str__(self):
        return self.title

class Nation(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    product_img = models.ImageField(null=True,blank=True, upload_to="product_img/") 
    slug = models.SlugField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    info = RichTextField(blank=True,null=True) 
    price = models.DecimalField(decimal_places=3, max_digits=15)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    is_sell = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    