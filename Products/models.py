from django.db import models

# Create your models here.

class Product(models.Model):

    KILOGRAM = 'Kilogram'
    GRAM = 'gram'
    LITER = 'liter'
    DESILITER = 'desiliter'
    MILLILITER = 'milliliter'
    UNITS = ((KILOGRAM, 'kg'), (GRAM, 'g'), (LITER, 'l'), (DESILITER, 'dl'), (MILLILITER, 'ml'))

    #Fields
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mass = models.DecimalField(max_digits=10, decimal_places=2)
    massUnit = models.CharField(max_length=150, choices=UNITS)
    vegetarian = models.BooleanField()
    vegan = models.BooleanField()

    #Relations
    producer = models.ForeignKey('Producer')
    productTypes = models.ManyToManyField('ProductType', blank=True, null=True)

    def __unicode__(self):
        return self.name + ' kr.' + str(self.price)

    def normalized_mass_unit(self):
        """ Returns a tuple with (0.5,  KILOGRAM)"""
        if(self.massUnit == self.GRAM):
            return (self.mass/1000, self.KILOGRAM)
        elif (self.massUnit == self.DESILITER):
            return (self.mass/10, self.LITER)
        elif (self.massUnit == self.MILLILITER):
            return (self.mass/1000, self.LITER)
        else:
            return (self.mass, self.massUnit)

    def price_per_mass(self):
        """ """
        mass, unit = self.normalized_mass_unit()
        return (self.price/mass, unit)

    def pretty_price_per_mass(self):
        price, unit = self.price_per_mass()
        return u'{price} kr/{unit}'.format(price=price, unit=unit)



class Producer(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
