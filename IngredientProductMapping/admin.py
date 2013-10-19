# coding=UTF-8
from django.contrib import admin
from IngredientProductMapping.models import QuantityType, IngredientProductMapping


admin.site.register(QuantityType)
admin.site.register(IngredientProductMapping)

