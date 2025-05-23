from django.contrib import admin

from products.models import Customer, Order, Product

#registramos los modelos en el admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'image')
    list_filter = ('name',)
    search_fields = ('name', 'stock')

#registramos el modelo Customer en el admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

#registramos el modelo Order en el admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date')
    

