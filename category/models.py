from django.db import models
from django.urls import reverse



class Category(models.Model):
    name_category = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=60, blank =True)
    
    class Meta:
        verbose_name ='category'
        verbose_name_plural ='categories'
    def __str__(self):
        return self.name_category

    def get_url(self):
         return reverse('products_by_category', args=[self.slug])


class SubCategory(models.Model):
    name_subCategory = models.CharField(max_length=60, unique =True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(max_length=60, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name ='sub_category'
        verbose_name_plural ='sub_categories'
    def __str__(self):
        return self.name_subCategory


class Shelf(models.Model):
    num_Shelf = models.CharField(max_length=60, primary_key=True)
    slug = models.SlugField(max_length=60,blank= True)
    description = models.TextField(max_length=60, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        verbose_name ='Shelf'
        verbose_name_plural = 'shelfs'

    def __str__(self):
        return self.num_Shelf