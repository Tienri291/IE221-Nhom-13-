from distutils.command.upload import upload
import imp
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

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