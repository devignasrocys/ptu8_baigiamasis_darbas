from django.db import models
from core.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_address", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self) -> str:
        return self.address1


class Order(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.PROTECT,related_name="orders")
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')

    def __str__(self) -> str:
        return f'Order id: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveBigIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_items', null=True, blank=True)

    def __str__(self) -> str:
        return f'Order item id: {self.id}'