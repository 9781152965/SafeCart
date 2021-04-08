from django.contrib import admin
from .models import Product, Contact, Order, OrderUpdate, Category,  item2


class AdminProduct(admin.ModelAdmin):
    list_display = ['product_id','product_name', 'category','price']

class AdminOrderUpdate(admin.ModelAdmin):
    list_display = ['order_id' , 'timestamp']

class AdminOrder(admin.ModelAdmin):
    list_display = ['name', 'order_id', 'address',]


# Register your models here.

admin.site.register(Product , AdminProduct)
admin.site.register(Contact)
admin.site.register( item2)
admin.site.register(Category)
admin.site.register(Order , AdminOrder)
admin.site.register(OrderUpdate , AdminOrderUpdate)