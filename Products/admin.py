__author__ = 'orjan'

from django.contrib import admin
from Products.models import Product, Producer, ProductType

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'price', 'producer', 'mass', 'massUnit', 'description' , 'vegetarian', 'vegan']

admin.site.register(Product, ProductAdmin)
admin.site.register(Producer)
admin.site.register(ProductType)