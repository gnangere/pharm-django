from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name_product',)}
    list_display =('name_product', 'slug','form','dosage','stock', 'price', 'is_available','in_amo', 'modified_date', 'created_date','category', 'image')




admin.site.register(Product, ProductAdmin)