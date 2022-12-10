from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name_product = models.CharField(max_length=60, unique = True)
    slug = models.SlugField(max_length=60, unique = True)
    description = models.TextField(max_length=255, blank = True)
    FORM_CHOICES = (
        ("FL", "FLACON"),
        ("BT", "BOITE"),
        ("TB", "TUBE"),
        ("CT", "CARTON"),

    )
    form = models.CharField(max_length=20, choices=FORM_CHOICES, default="BOITE")
    dosage = models.CharField(max_length=60,blank =True)
    price = models.FloatField(default =0.0)
    is_available = models.BooleanField(default=True)
    in_amo= models.BooleanField(default = False)
    stockMin = models.IntegerField(null =True)
    stockMax = models.IntegerField(null =True)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete =models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/products', blank =True)

    def __str__ (self):
        return self.name_product

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
