from decimal import Decimal as D

from django.contrib import admin

from products.models import (
    Category, 
    Customer, 
    Order, 
    OrderDetail,
    OrderDetailAuditLog,
    Product,
)

#registramos los modelos en el admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'image', 'category')
    list_filter = ('name','category')
    search_fields = ('name', 'stock')

    actions = ['update_price_15']

    def update_price_15(self, request, queryset):
        for product in queryset:
            product.price = product.price * D(1.15)  # Aumenta el precio en un 15%
            product.save()
        self.message_user(request, "se proceso correctamente el aumento del precio.", level='success')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

#registramos el modelo Customer en el admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

#registramos el modelo Order en el admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date')


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')


@admin.register(OrderDetailAuditLog)
class OrderDetailAuditLogAdmin(admin.ModelAdmin):
    list_display = ['order_detail', 'product_name', 'quantity', 'timestamp', 'action']
    readonly_fields = list_display

