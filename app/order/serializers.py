from rest_framework import serializers

from shop.models import Items
from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    total_items_price = serializers.ReadOnlyField(source='total_price')

    @property
    def total_price(self):
        all_price = Items.pbjects.filter(price=self)
        total = 0
        for price in all_price:
            total += price
        return total

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['created', ]
