from Products.models import Product
from django.db import models


class Cart(models.Model):
    created_at = models.DateTimeField(auto_created=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def add(self, product_id, quantity):
        if self._product_is_already_in_cart(product_id):
            self._add_quantity_to_cart(product_id, quantity)
        else:
            self._add_product_to_cart(product_id, quantity)

    def set(self, product_id, quantity):
        """ Update the cart in accordance with the parameters.
         If quantity is 0 the product is removed from the cart.
         Otherwise the product will be added to the cart with the given quantity.
        """
        if self._product_is_already_in_cart(product_id):
            if quantity <= 0:
                self._remove_product_from_cart(product_id)
            else:
                self._update_quantity_in_cart(product_id, quantity)
        else:
            self._add_product_to_cart(product_id, quantity)

    def _product_is_already_in_cart(self, product_id):
        return self.items.filter(product_id=product_id).exists()

    def _remove_product_from_cart(self, product_id):
        self.items.get(product_id=product_id).delete()

    def _update_quantity_in_cart(self, product_id, quantity):
        cart_item = self.items.get(product_id=product_id)
        cart_item.quantity = quantity
        cart_item.save()

    def _add_quantity_to_cart(self, product_id, quantity):
        cart_item = self.items.get(product_id=product_id)
        cart_item.quantity += quantity
        cart_item.save()

    def _product_exists(self, product_id):
        return Product.objects.filter(id=product_id).exists()

    def _add_product_to_cart(self, product_id, quantity):
        if quantity > 0 and self._product_exists(product_id):
            new_cart_item = CartItem(cart=self,
                                     product_id=product_id,
                                     quantity=quantity)
            new_cart_item.save()

    def __unicode__(self):
        return unicode(self.id)


class CartItem(models.Model):
    added_at = models.DateTimeField(auto_created=True, null=True)
    cart = models.ForeignKey(Cart, related_name='items')
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()

    def __unicode__(self):
        if self.quantity > 1:
            return u'{quantity} stk. {product}'.format(quantity=self.quantity,
                                                       product=self.product.name)
        else:
            return u'{product}'.format(product=self.product.name)