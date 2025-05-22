from django import forms

from products.models import (
    Customer,
    Order,
    OrderDetail,
    Product,
)

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['name', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Precio'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Stock'}),
            
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del cliente'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer']

        widgets = {
            'customer': forms.Select(
                attrs={'class': 'form-control'}
            )
        }


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['order', 'product', 'quantity']

        widgets = {
            'order': forms.HiddenInput(),
            'product': forms.Select(
                attrs={'class': 'form-control w-50'}
            ),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control w-25'}
            )
        }