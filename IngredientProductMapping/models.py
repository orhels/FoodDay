from django.db import models


KILOGRAM = 'kg'
GRAM = 'g'
LITER = 'l'
DESILITER = 'dl'
MILLILITER = 'ml'
UNITS = ((KILOGRAM, 'kilogram'), (GRAM, 'gram'), (LITER, 'liter'), (DESILITER, 'desiliter'), (MILLILITER, 'milliliter'))


def choose_cheapest_product(ingredient_quantity, product_list):
    #product_list = [(price per unit, id, price, quantity)]

    #Setup
    cur_list_index = 0
    reached_quantity = 0
    quantity_left = ingredient_quantity
    QUANTITY = 3
    PRICE = 2
    ID = 1
    result = {}

    # 1: take as many as you can of the cheapest (lowest unit price)
    for product in product_list:
        #setup
        product_quantity = product[QUANTITY]
        product_id = product[ID]
        #Add to cart if quantity is lower than remaining quantity
        if product_quantity <= quantity_left:
            number_of_products = quantity_left / product_quantity
            quantity_left -= number_of_products * product_quantity
            result.update({product_id: number_of_products})
            break


    # 2: try all permutations to fill up the remaining
    best_price = 999999999
    best_product = None
    for product in product_list:
        if product[QUANTITY] >= quantity_left:
            if product[PRICE] < best_price:
                best_price = product[PRICE]
                best_product = product[ID]
    result.update({best_product: 1})
    return result


class IngredientProductMapping(models.Model):
    #Fields
    name = models.CharField(max_length=150)

    def get_products_for_cart(self, total_ingredient_quantity, ingredient_quantity_type):
        ingredient_quantity = ingredient_quantity_type.get_quantity_multiplier_converter() * total_ingredient_quantity
        product_list = []
        for product in self.products:
            product_quantity = product.quantityType.get_quantity_multiplier_converter() * product.quantity
            product_list.append((product.price/product_quantity, product.id, product.price, product_quantity))
        product_list.sort()
        return choose_cheapest_product(ingredient_quantity, product_list)




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
