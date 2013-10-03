__author__ = 'orjan'

from django.contrib import admin
from Products.models import Product, Producer, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'price', 'producer', 'mass', 'massUnit', 'description', 'vegetarian', 'vegan']
    filter_horizontal = ['productCategories']

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'productCategories':
            kwargs['queryset'] = ProductCategory.objects.filter(children=None)
        return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Product, ProductAdmin)
admin.site.register(Producer)
admin.site.register(ProductCategory)