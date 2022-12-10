
from django.contrib import admin
from .models import Category, SubCategory, Shelf




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name_category',)}
    list_display = ('name_category', 'slug', 'description')

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name_subCategory',)}
    list_display = ('name_subCategory', 'slug','category')

class ShelfAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('num_Shelf',)}
    list_display = ('num_Shelf', 'slug')




admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Shelf, ShelfAdmin)