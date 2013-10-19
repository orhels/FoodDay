# Create your models here.
from django.db import models
from IngredientProductMapping.models import IngredientProductMapping, QuantityType


class Recipe(models.Model):
    #Fields
    name = models.CharField(max_length=300)
    description = models.TextField()
    procedure = models.TextField()
    servings = models.IntegerField()
    processing_time = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='height 400px, width 326px', upload_to='recipe_images',
                              default='recipe_images/recipe_images_placeholder.png', blank=True)

    #Relations
    ingredients = models.ManyToManyField(Ingredient)
    recipe_categories = models.ManyToManyField('RecipeCategory', blank=True, null=True, related_name='recipes')

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    #Fields
    name = models.CharField(max_length=150)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    is_main_ingredient = models.BooleanField(default=False)

    #Relations
    product = models.ForeignKey(IngredientProductMapping)
    quantityType = models.ForeignKey(QuantityType)

    def __unicode__(self):
        return self.name


class RecipeCategory(models.Model):
    #Fields
    name = models.CharField(max_length=150)

    #Relations
    parents = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='children')

    def __unicode__(self):
        return self.name
