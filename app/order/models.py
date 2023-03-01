from django.db import models

from shop.models import Items


class OrderItem(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Order(models.Model):
    order_item = models.ManyToManyField(OrderItem)
    created = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True, blank=True)
