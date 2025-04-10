#products_services
from products.models import Product
from products.repositories.products import ProductRepository

class ProductService:
    """
    Clase de servicio que se encargara de manipular los productos
    """

    """
    se puede utilizar con el init ,y necesitan pasar siempre self
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository


    def get_all(self) -> list[Product]:
        
        return self.product_repository.get_all()
    """
    
    @staticmethod
    def get_all() -> list[Product]:
        """
        Obtiene todos los productos
        """
        return ProductRepository.get_all()
    
    @staticmethod
    def delete(product_id: int) -> bool:
        product = ProductRepository.get_by_id(product_id=product_id) #obtiene el producto y una vez que lo tiene lo elimina
        if product: 
            return ProductRepository.delete(product=product)
        return False
    
    @staticmethod
    def update(product_id:int, price: float, stock: int,) -> bool:
        product = ProductRepository.get_by_id(product_id=product_id) #obtiene el producto y una vez que lo tiene lo actualiza
        if product:
            return ProductRepository.update(product=product, price=price, stock=stock,)
        
        