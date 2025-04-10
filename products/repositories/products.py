#products_repositories
from products.models import Product

class ProductRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manipular los productos
    """
    
    @staticmethod
    # Crear un producto
    def create(name: str, price: float, stock:int) -> Product:

        return Product.objects.create(
            name=name, 
            price=price, 
            stock=stock
        )
    
    @staticmethod
    # borra un producto
    def delete(product: Product) -> bool:
        try:
            Product.delete()
        except Product.DoesNotExist:
            raise ValueError("El producto no existe")


    @staticmethod
    def update(product: Product, price: float, stock: int) -> Product:
        """
        Actualiza un producto
        """
        product.price = price
        product.stock = stock
        product.save()
        return product
            


    @staticmethod
    def get_all() -> list[Product]:
        """
        Obtiene todos los objectos (Product)
        """
        return Product.objects.all()   
    
    @staticmethod
    def get_by_id(product_id: int) -> Product:
        """
        Obtiene un producto a partir de su id
        """
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None
    
    @staticmethod
    def search_by_name(name: str) -> list[Product]:
        """
        Busca los products que contengan el nombre ingresado
        """
        return Product.objects.filter(name__icontains=name)
        ##############################atributro_que_contenga_cadena_que_le_paso


    @staticmethod
    def filter_by_price_range(min_price: float, max_price: float) -> list[Product]:
        """
        Retorna un listado de productos cuyo precio esta en el rango establecido
        """
        return Product.objects.filter(price__range=(min_price, max_price)) #incluye el minimo y el maximo
        #podemos usar cualquiera de las dos(range incluye los extremos al igual que gte y lte)
        return Product.objects.filter(price__gte=min_price, price__lte=max_price)