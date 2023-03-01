from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import CategoryListView, CategoryRetrieve, ItemsListView,  ItemRetrieve, ItemsCategoryListView

item_router = DefaultRouter()


urlpatterns = [
    path('', ItemsListView.as_view()),
    path('<int:pk>/', ItemRetrieve.as_view()),

    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryRetrieve.as_view()),
    path('category/<int:category_id>/items/', ItemsCategoryListView.as_view()),


]
