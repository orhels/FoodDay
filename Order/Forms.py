# coding=UTF-8
from django.forms import ModelForm

from .models import Order, Address


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['email',
                  'phone_number',
                  'phone_number_extra']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['first_name',
                  'last_name',
                  'street',
                  'postal_code',
                  'postal_place']