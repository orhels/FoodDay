from django.db import models


KILOGRAM = 'kg'
GRAM = 'g'
LITER = 'l'
DESILITER = 'dl'
MILLILITER = 'ml'
UNITS = ((KILOGRAM, 'kilogram'), (GRAM, 'gram'), (LITER, 'liter'), (DESILITER, 'desiliter'), (MILLILITER, 'milliliter'))


class IngredientProductMapping(models.Model):
    #Fields
    name = models.CharField(max_length=150)

    def get_products_for_cart(self, total_ingredient_quantity, ingredient_quantity_type):
        ingredient_quantity = ingredient_quantity_type.get_quantity_multiplier_converter() * total_ingredient_quantity
        for product in self.products:
            product.quantityType.get_quantity_multiplier_converter() * product.quantity
            # todo
            [('product_id', 'pris', 'vekt'), (),()]



class QuantityType(models.Model):
    name = models.CharField(max_length=25, choices=UNITS)
    category = models.CharField(max_length=30, choices=(('vekt', 'vekt'),
                                                        ('volum', 'volum'),
                                                        ('antall', 'antall')))

    def __unicode__(self):
        return self.name

    def get_quantity_multiplier_converter(self):
        ratios = {'KILOGRAM': 1000,
                  'DESILITER': 100,
                  'LITER': 1000}
        return ratios.get(self.name, 1)

    def get_normalized_mass_unit(self, quantity):
        """ Returns a tuple with (0.5,  KILOGRAM)"""
        if self.name == GRAM:
            return quantity / 1000, KILOGRAM
        elif self.name == DESILITER:
            return quantity / 10, LITER
        elif self.name == MILLILITER:
            return quantity / 1000, LITER
        else:
            return quantity, self.name
