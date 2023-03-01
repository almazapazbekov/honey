from rest_framework import serializers

from .models import Category, Items


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        exclude = ['description', ]


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"



