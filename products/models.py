from django.db import models

# Create your models here.

#este product es el producto que se va a vender
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


#este customer es el cliente que hace el pedido   
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


#este order es el pedido que hace un cliente
class Order(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)


#esto es el detalle del pedido, es decir, los productos que se piden
class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE,
        related_name='details',
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} - {self.product}"