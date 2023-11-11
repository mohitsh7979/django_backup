from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','price','catagory','images']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']


@admin.register(Orderplaced)
class OrderplacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity']




