# coding=UTF-8
from Cart.models import Cart, CartItem
from django.contrib import admin


class CartItemInline(admin.StackedInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ('id', 'last_updated', 'belongs_to_order')

admin.site.register(Cart, CartAdmin)