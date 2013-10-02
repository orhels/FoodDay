__author__ = 'orjan'

from django.contrib import admin
from Products.models import Product, Producer, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'price', 'producer', 'mass', 'massUnit', 'description', 'vegetarian', 'vegan']
    filter_horizontal = ['productCategories']

admin.site.register(Product, ProductAdmin)
admin.site.register(Producer)
admin.site.register(ProductCategory)