# coding=UTF-8
from Cart.models import Cart, CartItem
from django.contrib import admin


class CartItemInline(admin.StackedInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)