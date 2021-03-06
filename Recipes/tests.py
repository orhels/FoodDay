# coding=UTF-8
from django.test import TestCase
from IngredientProductMapping.models import choose_cheapest_product


class TestRecipe(TestCase):
    #def setUp(self):
    #    self.carbonaraRecipe = Recipe(
    #        name="Carbonara",
    #        description="",
    #        procedure="",
    #        servings=4,
    #        processing_time="",
    #        image="",
    #    )
    #    self.carbonaraRecipe.save()
    #
    #    self.gramQT = QuantityType(
    #        name=GRAM,
    #        category='vekt'
    #    )
    #    self.gramQT.save()
    #
    #    self.producer = Producer(
    #        name="Toro"
    #    )
    #    self.producer.save()
    #
    #    self.pastaProduct = Product(
    #        name="pasta",
    #        description="",
    #        price=35,
    #        quantity=120,
    #        image="",
    #        quantityType=self.gramQT,
    #        producer=self.producer,
    #    )
    #    self.pastaProduct.save()
    #
    #    self.pastaIngredient = Ingredient(
    #        name="pasta",
    #        quantity=550,
    #        recipe=self.carbonaraRecipe,
    #        quantityType=self.gramQT
    #    )
    #    self.pastaIngredient.save()
    #
    #    self.pastaIngredientMapping = IngredientProductMapping(
    #        name="pasta")
    #    self.pastaIngredientMapping.save()
    #    self.pastaIngredientMapping.ingredient.add(self.pastaIngredient)
    #    self.pastaIngredientMapping.product.add(self.pastaProduct)
    #    self.pastaIngredientMapping.save()
    #
    #
    #def test_get_products_for_cart(self):
    #    self.assertEqual(
    #        self.carbonaraRecipe.get_products_for_cart(3),
    #        {'1': 8})

    def test_choose_cheapest_product(self):
        self.assertEqual(
            choose_cheapest_product(800,
                        [
                           #(price per unit, id, price, quantity)
                            (0.1,    'stor pakke',         120, 1200),
                            (0.17,   'mellomstor pakke',   70,  400),
                            (0.25,   'liten pakke',        50,  200)
                        ]),
            {'stor pakke': 1}
        )
        self.assertEqual(
            choose_cheapest_product(100,
                        [
                           #(price per unit, id, price, quantity)
                            (0.1,    'stor pakke',         120, 1200),
                            (0.17,   'mellomstor pakke',   70,  400),
                            (0.25,   'liten pakke',        50,  200)
                        ]),
            {'liten pakke': 1}
        )
        self.assertEqual(
            choose_cheapest_product(3000,
                        [
                           #(price per unit, id, price, quantity)
                            (0.1,    'stor pakke',         120, 1200),
                            (0.17,   'mellomstor pakke',   70,  400),
                            (0.25,   'liten pakke',        50,  200)
                        ]),
            {'stor pakke': 3}
        )
        self.assertEqual(
            choose_cheapest_product(600,
                                    [
                                        (0.291, 'stor pakke',       350, 1200),
                                        (0.333, 'liten pakke',      100,  300),
                                        (0.375, 'mellomstor pakke', 150, 400)
                                    ]),
            {'liten pakke': 2}
        )

    def test_choose_cheapest_product_hard(self):
        self.assertEqual(
            choose_cheapest_product(600,
                                    [
                                        (0.300, 'stor pakke',       350, 1200),
                                        (0.375, 'mellomstor pakke', 150, 400),
                                        (0.450, 'liten pakke',      90,  200)
                                    ]),
            {'liten pakke': 1, 'mellomstor pakke': 1}
        )

        self.assertEqual(
            choose_cheapest_product(10001,
                                    [
                                        (0.1, 'mega pakke',         1000, 10000),
                                        (0.3, 'stor pakke',         300, 1000),
                                        (10.0, 'liten pakke',        10, 1)
                                    ]),
            {'mega pakke': 1, 'liten pakke': 1}
        )

        self.assertEqual(
            choose_cheapest_product(10700,
                                    [
                                        (0.1, 'mega pakke',         1000, 10000),
                                        (0.3, 'stor pakke',         300, 1000),
                                        (10.0, 'liten pakke',        10, 1)
                                    ]),
            {'mega pakke': 1, 'stor pakke': 1}
        )
        # this one takes a lot of time.
        self.assertEqual(
            choose_cheapest_product(11701,
                                    [
                                        (0.1, 'mega pakke',         1000, 10000),
                                        (0.3, 'stor pakke',         300, 1000),
                                        (10.0, 'liten pakke',        10, 1)
                                    ]),
            {'mega pakke': 1, 'stor pakke': 2}
        )

        self.assertEqual(
            choose_cheapest_product(11701,
                                    [
                                        (10.0, 'mega pakke',         1000, 100),
                                        (10.0, 'liten pakke',        10, 1),
                                        (30.0, 'stor pakke',         300, 10)
                                    ]),
            {'mega pakke': 117, 'liten pakke': 1}
        )



