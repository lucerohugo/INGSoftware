from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['name', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Precio'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Stock'}),
            
        }