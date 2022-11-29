from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # Method 1: Using exceptions to catch objects not existing
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass

    # Method 2: Using filters to detect objects' existence
    exists = Product.objects.filter(pk=0).exists()
    product = Product.objects.filter(pk=0).first()

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe"})
