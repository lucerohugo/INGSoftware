from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        """
        Metodo que se ejecuta cuando la app esta lista
        Importante aqui los signals evita problemas de importacion
        """
        from products import signals
        return super().ready()
