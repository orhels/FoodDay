from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from Cart.models import Cart

from .forms import OrderForm, AddressForm


def handle_order_form(request):
    if request.method == 'GET':
        return _render_blank_form(request)
    elif request.method == 'POST':
        order_form = OrderForm(request.POST, prefix='order_form')
        shipping_form = AddressForm(request.POST, prefix='shipping_form')
        if order_form.is_valid() and shipping_form.is_valid():
            return _update_models_and_return_success(order_form, request, shipping_form)
        else:
            return _render_form_with_errors(request, order_form, shipping_form)


def _render_blank_form(request):
    dictionary = csrf(request)
    dictionary.update({'order_form': OrderForm(prefix='order_form'),
                       'shipping_form': AddressForm(prefix='shipping_form')})
    return render(dictionary)


def _update_models_and_return_success(order_form, request, shipping_form):
    shipping_form_saved = shipping_form.save()
    order_form_saved = order_form.save(commit=False)
    order_form_saved.shipping_address = shipping_form_saved
    #todo: determine shipping cost
    order_form_saved.shipping_cost = 0
    order_form_saved.cart = Cart.objects.clone_cart(request)
    order_form_saved.save()
    return HttpResponse("success")


def _render_form_with_errors(request, order_form, shipping_form):
    dictionary = csrf(request)
    dictionary.update({'order_form': order_form,
                       'shipping_form': shipping_form})
    return render(dictionary)


def render(dictionary):
    return render_to_response('order_form.html',
                              dictionary)

