from django.urls import path

from . import views


urlpatterns = [
    path('item/', views.OrderItemListCreateAPIView.as_view()),
    path('', views.OrderListCreateAPIView.as_view()),
]
