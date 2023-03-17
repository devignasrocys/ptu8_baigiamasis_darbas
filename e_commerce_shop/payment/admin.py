from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'address1', 'address2', 'state', 'zipcode', 'user',]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'shipping_address', 'amount_paid', 'date_ordered', 'user',]



