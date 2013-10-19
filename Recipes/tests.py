# coding=UTF-8
from django.test import TestCase
from IngredientProductMapping.models import QuantityType, GRAM, IngredientProductMapping
from Products.models import Product, Producer

from Recipes.models import Recipe, Ingredient


class TestRecipe(TestCase):
    def setUp(self):
        self.carbonaraRecipe = Recipe(
            name="Carbonara",
            description="",
            procedure="",
            servings=4,
            processing_time="",
            image="",
        )
        self.carbonaraRecipe.save()

        self.gramQT = QuantityType(
            name=GRAM,
            category='vekt'
        )
        self.gramQT.save()

        self.producer = Producer(
            name="Toro"
        )
        self.producer.save()

        self.pastaProduct = Product(
            name="pasta",
            description="",
            price=35,
            quantity=120,
            image="",
            quantityType=self.gramQT,
            producer=self.producer,
        )
        self.pastaProduct.save()

        self.pastaIngredient = Ingredient(
            name="pasta",
            quantity=550,
            recipe=self.carbonaraRecipe,
            quantityType=self.gramQT
        )
        self.pastaIngredient.save()

        self.pastaIngredientMapping = IngredientProductMapping(
            name="pasta")
        self.pastaIngredientMapping.save()
        self.pastaIngredientMapping.ingredient.add(self.pastaIngredient)
        self.pastaIngredientMapping.product.add(self.pastaProduct)
        self.pastaIngredientMapping.save()


    def test_get_products_for_cart(self):
        self.assertEqual(
            self.carbonaraRecipe.get_products_for_cart(3),
            {'1': 8})
