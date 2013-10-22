from django.db import models
import itertools


KILOGRAM = 'kg'
GRAM = 'g'
LITER = 'l'
DESILITER = 'dl'
MILLILITER = 'ml'
UNITS = ((KILOGRAM, 'kilogram'), (GRAM, 'gram'), (LITER, 'liter'), (DESILITER, 'desiliter'), (MILLILITER, 'milliliter'))


def choose_cheapest_product(ingredient_quantity, product_list):
    #product_list = [(price per unit, id, price, quantity)]

    #Setup
    quantity_left = int(ingredient_quantity)
    QUANTITY = 3
    ID = 1
    result = {}

    # 1: take as many as you can of the cheapest (lowest unit price)
    # TODO: maybe we should check if the list is sorted?
    product = product_list[0]
    product_quantity = int(product[QUANTITY])
    product_id = product[ID]
    if product_quantity <= quantity_left:
        number_of_products = quantity_left / product_quantity
        quantity_left -= number_of_products * product_quantity
        result.update({product_id: number_of_products})

    if quantity_left == 0:
        return result
    combinations = []
    combination_choices = product_list

    # 2: First we need to create all combinations that fulfills the required quantity, but has no "extra" products.
    combination_length = 1
    while combination_choices:
        disapproved_combinations = []
        temp_comb = itertools.combinations_with_replacement(combination_choices, combination_length)
        for comb in temp_comb:
            comb = list(comb)
            # If the combination fulfills the required quantity
            if quantity_of_combination(comb) >= quantity_left:
                combinations.append(comb)
            else:
                disapproved_combinations.append(comb)

        # checks if all of the disapproved_combinations are worse then the best combination we have so far.
        # If all are worse we can stop execution because it will never choose
        # any combination where this is a subcombination, as you always add another product.
        comb_min = 99999999999999999
        for comb in combinations:
            if price_of_combination(comb) < comb_min:
                comb_min = price_of_combination(comb)
        abort = True
        for comb in disapproved_combinations:
            if price_of_combination(comb) < comb_min:
                abort = False
        if abort:
            break
        # if a product does not exists in the disapproved_combinations, then it must exist in every accepted combination
        # and we can exclude it from any further combinations
        combination_choices[:] = [x for x in combination_choices if product_exists_in(x, disapproved_combinations)]
        combination_length += 1

    # 3: Then we must select the best combination
    combinations = sorted(combinations, key=lambda combination: price_of_combination(combination))
    for product in combinations[0]:
        if product[ID] in result:
            result[product[ID]] += 1
        else:
            result.update({product[ID]: 1})
    print "Result", result
    return result


def product_exists_in(product, dissaproved_combinations):
    if not dissaproved_combinations:
        return False
    for comb in dissaproved_combinations:
        if product in comb:
            return True
    return False


def quantity_of_combination(perm):
    q = 0
    for p in perm:
        q += p[3]
    return q


def price_of_combination(perm):
    price = 0
    for p in perm:
        price += p[2]
    return price


class IngredientProductMapping(models.Model):
    #Fields
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

    def get_products_for_cart(self, total_ingredient_quantity, ingredient_quantity_type):
        ingredient_quantity = int(ingredient_quantity_type.get_quantity_multiplier_converter() * total_ingredient_quantity)
        product_list = []
        for product in self.products.all():
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
