from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')
    exclude = ('last_modification', )

    def __str__(self):
        return self.name    

admin.site.register(Product, ProductAdmin)