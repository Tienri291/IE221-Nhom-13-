from distutils.command.upload import upload
import imp
from lib2to3.refactor import MultiprocessingUnsupported
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
#lass UserManager(BaseUserManager):
#    def create_user(self,email,password=None,is_active = True, is_staff=False,is_admin=False):
#        if not email:
#            raise ValueError("Bạn phải nhập email")
#        if not password:
#            raise ValueError("Bạn phải nhập password")
#
#       user_obj = self.model(
#            email = self.normalize_email(email)
#        )
#        user_obj.set_password(password)
#        user_obj.staff = is_staff
#        user_obj.admin = is_admin
#        user_obj.active = is_active
#        user_obj.save(using = self._db)
#        return user_obj

#    def create_staffuser(self,email,password=None):
#        user = self.create_user(
#            email,
#            password = password,
#            is_active= True
#        )

#    def create_superuser(self,email,password=None):
#        user = self.create_user(
#           email,
#            password = password,
#            is_active= True
#        )

#class CustomUser(AbstractBaseUser):
#    first_name = models.CharField(max_length=255)
#    last_name = models.CharField(max_length=255)  
#    username = models.CharField(max_length=255)
#    email = models.EmailField(max_length=255,unique=True)
#    active = models.BooleanField(default=True)
#    staff = models.BooleanField(default=False)
#    admin = models.BooleanField(default=False)
    
#    REQUIRED_FIELDS = [username,email]

#    def __str__(self):
#        return self.username

#    def full_name(self):
#        return self.first_name + ' ' + self.last_name

#    @property
#    def is_staff(self):
#        return self.staff

#    @property
#    def is_active(self):
#        return self.active

#    @property
#    def is_admin(self):
#        return self.admin

#class Customer(models.Model):
#    user = models.OneToOneField(User)


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
 
