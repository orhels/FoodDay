"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from Products.models import Product, Producer
from django.core.urlresolvers import reverse

from django.test import TestCase, Client


class ProductTest(TestCase):

    def setUp(self):
        self.producer = Producer(name='Tine meierier')
        self.producer.save()
        self.product = Product(name='Jarlsberg med 27% fett',
                               price=121.,
                               mass=700.,
                               massUnit=Product.GRAM,
                               producer=self.producer)
        self.product.save()

    def test_product_detail_view_should_contain_the_correct_data(self):
        client = Client()
        response = client.get(reverse('product_detail', args=[self.product.id]))
        self.assertContains(response, 'Jarlsberg med 27% fett')
        self.assertContains(response, '121')
        self.assertContains(response, '700')
        self.assertContains(response, Product.GRAM)
        self.assertContains(response, 'Tine meierier')
        self.assertContains(response, '172.86 kr/kg')

    def test_pretty_price_per_mass(self):
        self.assertEqual(self.product.pretty_price_per_mass(), u'172.86 kr/kg')