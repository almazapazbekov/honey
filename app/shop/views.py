from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Items, Category
from .serializers import CategorySerializer, ItemListSerializer, ItemDetailSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieve(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemsListView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemListSerializer


class ItemsCategoryListView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemListSerializer

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs.get('category_id'))


class ItemRetrieve(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemDetailSerializer







