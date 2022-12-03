from django.shortcuts import render
from django.db.models import F
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(
        orderitem__product=F("pk")).distinct().order_by("title")

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "products": queryset})
