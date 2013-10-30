# coding=UTF-8
from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', 'email_has_been_sent', )

admin.site.register(Order, OrderAdmin)