from django.shortcuts import render, get_list_or_404

from products.models import Product
from products.services.products import ProductService

def product_list(request):
    all_products = ProductService.get_all()
    total_price = ProductService.sum_total_price(all_products)

    return render(
        request,  
        'products/list.html',
        dict(
            products = all_products,
            otro_atributo= 'Atributo 2',
            total_price = total_price 
        )
    )

def product_detail(request, product_id):
    product= get_list_or_404(Product, id=product_id)
    return render(
        request,
        'products/detail.html',
        dict(
            product= product,
        )
    )

def order_list(request):
    return render(request, 'orders/list.html')

