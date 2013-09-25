from django.db import models

# Create your models here.

class Product(models.Model):
    #Fields
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    #Relations
    producer = models.ForeignKey('Producer')
    productTypes = models.ManyToManyField('ProductType', blank=True, null=True)

    def __unicode__(self):
        return self.name + ' kr.' + str(self.price)


class Producer(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name
