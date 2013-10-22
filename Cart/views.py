import json
from Cart.models import Cart
from django.http import HttpResponse
from django.shortcuts import render_to_response


def _get_or_create_cart(request):
    if request.session.has_key('cart_id'):
        cart = Cart.objects.get(pk=request.session['cart_id'])
    else:
        cart = Cart()
        cart.save()
        request.session['cart_id'] = cart.id
    return cart


def get_cart_widget(request):
    cart = _get_or_create_cart(request)
    return render_to_response('cart_widget.html', {'cart': cart})


def update_cart(request):
    product_id = int(request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    cart = _get_or_create_cart(request)
    cart.set(product_id, quantity)
    return HttpResponse(status=200)


def add_to_cart(request):
    print request.body
    products = json.loads(request.body)
    product_list = []
    for p in products:
        product_list.append((p['product_id'], p['quantity']))
    cart = _get_or_create_cart(request)
    cart.add(product_list)
    return HttpResponse(status=200)