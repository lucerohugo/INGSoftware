import csv

from django.contrib import admin

from home.models import FileUppload
from products.models import Category, Product

# Register your models here.

@admin.register(FileUppload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    actions = ['load_data_from_file']

    def load_data_from_file(self, request, queryset):
        for file_obj in queryset:
            if not file_obj.file.name.endswith('.csv'):
                self.message_user(request, "El archivo debe ser un CSV.{file.obj.file.name}", level='error')
                continue

            with open(file_obj.file.path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category, _  = Category.objects.get_or_create(
                        name=row['category']
                    )
                    Product.objects.create(
                        name=row['name'],
                        price=row['price'],
                        stock=row['stock'],
                        category=category
                    )
        self.message_user(request, "Datos cargados correctamente desde el archivo CSV.", level='success')
                
    
    load_data_from_file.short_description = "Cargar productos"
    
