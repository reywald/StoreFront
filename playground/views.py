from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    products = Product.objects.filter(inventory=F('collection__id'))

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe", "products": list(products)})
