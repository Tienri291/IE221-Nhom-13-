from django.contrib import admin
from .models import Post,Collection,Brand,Nation,Product,Tag

class PostAdmin(admin.ModelAdmin):
   list_display = ('id','title','header_image') 
admin.site.register(Post,PostAdmin)


admin.site.register(Collection)
admin.site.register(Brand)
admin.site.register(Nation)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(Tag,ProductAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','collection','price','is_sell')
    list_editable = ('is_sell',)
admin.site.register(Product,ProductAdmin)

