from django.contrib import admin
from .models import Product,Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','title',]
    list_display_links=['id','title',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id','title','category','price','available','created','updated']
    list_display_links = ['id','title']
    list_filter = [ 'category','status','created','updated']
    prepopulated_fields = {'slug':('title',)}

