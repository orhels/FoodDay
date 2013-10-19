from django.db import models
from IngredientProductMapping.models import QuantityType


class Product(models.Model):

    #Fields
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='height 400px, width 326px', upload_to='product_images',
                              default='product_images/product_images_placeholder.png', blank=True)

    #Relations
    quantityType = models.ForeignKey(QuantityType)
    producer = models.ForeignKey('Producer')
    productCategories = models.ManyToManyField('ProductCategory', blank=True, null=True, related_name='products')
    ingredientMapping = models.ForeignKey('IngredientProductMapping.IngredientProductMapping', related_name='products', blank=True, null=True)

    def __unicode__(self):
        return self.name + ' kr.' + str(self.price)

    def _price_per_mass(self):
        """ Returns a tuple with (price/weight, unit) """
        mass, unit = self.quantityType.get_normalized_mass_unit(self.quantity)
        return self.price/mass, unit

    def pretty_price_per_mass(self):
        """ Returns a string for displaying price per weight unit """
        price_mass, unit = self._price_per_mass()
        return u'{:.2f} kr/{unit}'.format(price_mass, unit=unit)

    def pretty_price(self):
        return u'{price},-'.format(price=self.price)


class Producer(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    parents = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='children')

    def __unicode__(self):
        return self.name

