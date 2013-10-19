from django.db import models

from Recipes.models import Ingredient
from Products.models import Product


KILOGRAM = 'kg'
GRAM = 'g'
LITER = 'l'
DESILITER = 'dl'
MILLILITER = 'ml'
UNITS = ((KILOGRAM, 'kilogram'), (GRAM, 'gram'), (LITER, 'liter'), (DESILITER, 'desiliter'), (MILLILITER, 'milliliter'))


class IngredientProductMapping(models.Model):
    #Fields
    name = models.CharField(max_length=150)

    #Relations
    ingredient = models.ManyToManyField(Ingredient)
    product = models.ManyToManyField(Product)


class QuantityType(models.Model):
    name = models.CharField(max_length=25, choices=UNITS)
    category = models.CharField(max_length=30, choices=(('vekt', 'vekt'),
                                                        ('volum', 'volum'),
                                                        ('antall', 'antall')))

    def get_normalized_mass_unit(self):
        """ Returns a tuple with (0.5,  KILOGRAM)"""
        if self.name == GRAM:
            return self.mass/1000, KILOGRAM
        elif self.name == DESILITER:
            return self.mass/10, LITER
        elif self.name == MILLILITER:
            return self.mass/1000, LITER
        else:
            return self.mass, self.name