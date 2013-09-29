from django.db import models


class Product(models.Model):

    KILOGRAM = 'kg'
    GRAM = 'g'
    LITER = 'l'
    DESILITER = 'dl'
    MILLILITER = 'ml'
    UNITS = ((KILOGRAM, 'kilogram'), (GRAM, 'gram'), (LITER, 'liter'), (DESILITER, 'desiliter'), (MILLILITER, 'milliliter'))

    #Fields
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mass = models.DecimalField(max_digits=10, decimal_places=2)
    massUnit = models.CharField(max_length=150, choices=UNITS)
    vegetarian = models.BooleanField()
    vegan = models.BooleanField()
    image = models.ImageField(verbose_name='height 400px, width 326px', upload_to='product_images',
                              default='product_images/product_images_placeholder.png', blank=True)

    #Relations
    producer = models.ForeignKey('Producer')
    productCategories = models.ManyToManyField('ProductCategory', blank=True, null=True)

    def __unicode__(self):
        return self.name + ' kr.' + str(self.price)

    def _normalized_mass_unit(self):
        """ Returns a tuple with (0.5,  KILOGRAM)"""
        if self.massUnit == self.GRAM:
            return self.mass/1000, self.KILOGRAM
        elif self.massUnit == self.DESILITER:
            return self.mass/10, self.LITER
        elif self.massUnit == self.MILLILITER:
            return self.mass/1000, self.LITER
        else:
            return self.mass, self.massUnit

    def _price_per_mass(self):
        """ Returns a tuple with (price/weight, unit) """
        mass, unit = self._normalized_mass_unit()
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
    parents = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='parent+')
    children = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='child+')

    def __unicode__(self):
        return self.name
