# Create your models here.
from django.db import models


class Recipe(models.Model):
    #Fields
    name = models.CharField(max_length=300)
    description = models.TextField()
    procedure = models.TextField()
    servings = models.IntegerField()
    processing_time = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='height 400px, width 326px', upload_to='recipe_images',
                              default='recipe_images/recipe_images_placeholder.png', blank=True)
    url = models.URLField(max_length=400)

    #Relations
    recipe_categories = models.ManyToManyField('RecipeCategory', blank=True, null=True, related_name='recipes')
    recipe_author = models.ForeignKey('RecipeAuthor', blank=True, null=True, related_name='recipes')

    def __unicode__(self):
        return self.name

    def get_products_for_cart(self, desired_servings):
        #  [(product_id, number_of_products), ]
        servings_ration = desired_servings / self.servings
        result = {}
        for ingredient in self.ingredients.all():
            result.update(ingredient.get_products_for_cart(servings_ration))
        return result


class Ingredient(models.Model):
    #Fields
    name = models.CharField(max_length=150)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    is_main_ingredient = models.BooleanField(default=False)
    is_added_by_default = models.BooleanField(default=False)

    #Relations
    recipe = models.ForeignKey('Recipe', related_name='ingredients')
    quantityType = models.ForeignKey('IngredientProductMapping.QuantityType')
    productMapping = models.ForeignKey('IngredientProductMapping.IngredientProductMapping', related_name='ingredients', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_products_for_cart(self, servings_ratio):
        total_quantity = float(self.quantity) * servings_ratio
        result = self.productMapping.get_products_for_cart(total_quantity, self.quantityType)
        for k, v in result.iteritems():
            result[k] = [v, self.is_added_by_default]
        return result


class RecipeCategory(models.Model):
    #Fields
    name = models.CharField(max_length=150)

    #Relations
    parents = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='children')

    def __unicode__(self):
        return self.name


class RecipeAuthor(models.Model):
    #Fields
    name = models.CharField(max_length=150)
    url = models.URLField(max_length=200)
    attribution_text = models.TextField()

    #Relations

    def __unicode__(self):
        return self.name