from django.db import models
from django.utils.timesince import timesince


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name='Epost')
    phone_number = models.CharField(max_length=15, verbose_name='Telefonnummer')
    phone_number_extra = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefonnummer 2 (valgfritt)')
    shipping_address = models.ForeignKey('Address', related_name='shippingaddress')
    email_has_been_sent = models.BooleanField(default=False)
    shipping_cost = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    cart = models.ForeignKey('Cart.Cart', related_name='order')
    delivery_time_from = models.DateTimeField()
    delivery_time_to = models.DateTimeField()

    def __unicode__(self):
        return u'Order {order_number} ({created} ago)'.format(order_number=self.pk,
                                                              created=self.time_since_order())

    def time_since_order(self):
        return timesince(self.created)

    def get_total_price(self):
        self.cart.get_total_price()

    def get_shipping_cost(self):
        return self.shipping_cost

    def get_total_price_with_shipping_cost(self):
        return self.get_total_price() + self.get_shipping_cost()


class Address(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Fornavn')
    last_name = models.CharField(max_length=200, verbose_name='Etternavn')
    street = models.CharField(max_length=300, verbose_name='Adresse')
    postal_code = models.CharField(max_length=4, verbose_name='Postnummer')
    postal_place = models.CharField(max_length=100, verbose_name='Poststed')

    def __unicode__(self):
        return u'{first_name} {last_name}, ' \
               u'{street}, ' \
               u'{postal_code} {postal_place}'.format(first_name=self.first_name,
                                                      last_name=self.last_name,
                                                      street=self.street,
                                                      postal_code=self.postal_code,
                                                      postal_place=self.postal_place)