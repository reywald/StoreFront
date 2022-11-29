from django.shortcuts import render
from store.models import Product


def say_hello(request):
    products = Product.objects.filter(collection__title="Stationary")

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "products": list(products)})
