"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from Products.models import Producer, Product
from django.core.urlresolvers import reverse

from django.test import TestCase, Client


class CartViewTest(TestCase):
    def test_cart_widget(self):
        self.assertEqual(1 + 1, 2)

    def setUp(self):
        self.producer = Producer(name='Tine meierier')
        self.producer.save()
        self.product = Product(name='Jarlsberg med 27% fett',
                               price=121.,
                               mass=700.,
                               massUnit=Product.GRAM,
                               producer=self.producer)
        self.product.save()

    def test_cart_widget(self):
        client = Client()
        client.post(reverse('cart_add'), {'product_id': self.product.id, 'quantity': 1})
        response = client.get(reverse('cart_widget'))
        self.assertContains(response, 'Jarlsberg med 27% fett')