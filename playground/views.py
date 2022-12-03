from django.shortcuts import render
from django.db.models import F
# from store.models import Product
from store.models import Order
from store.models import OrderItem


def say_hello(request):
    queryset = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "orders": queryset})