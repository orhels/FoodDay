from Cart.models import Cart
from django.shortcuts import render_to_response


def get_cart_widget(request):
    if request.session.has_key('cart_id'):
        cart = request.session['cart_id']
    else:
        cart = Cart()
        cart.save()
        request.session['cart_id'] = cart.id
    return render_to_response('cart_widget.html', {'cart': cart})