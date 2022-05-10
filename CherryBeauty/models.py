
import profile
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True, upload_to="images/blog/")
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextUploadingField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date_added']
    @property
    def headerimageURL(self):
        try:
            url = self.header_image.url
        except:
            url = ''
        return url

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)

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

class Tag(models.Model):
    title = models.CharField(max_length=255) 
    def __str__(self):
        return self.title 

class Product(models.Model):
    title = models.CharField(max_length=255)
    product_img = models.ImageField(null=True,blank=True, upload_to="product_img/") 
    slug = models.SlugField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE,blank=True,null=True)
    info = RichTextField(blank=True,null=True)
    body = RichTextUploadingField(blank=True,null=True) 
    price = models.DecimalField(decimal_places=3, max_digits=15)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True) 
    is_sell = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/customer/profile_pic")
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=255,null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True, null=True) # validators should be a list

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.oderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.oderitem_set.all()
        total = sum([item.quantily for item in orderitems])
        return total 

class OderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantily = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantily
        return total

class City(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True)
    state = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address 

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)