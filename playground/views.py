from django.shortcuts import render
from store.models import Product, Collection


def say_hello(request):
    # product = Product.objects.get(pk=11)
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    Collection.objects.filter(pk=11).update(featured_product=None, title="Games")

    return render(request, "hello.html", {"name": "Ikechukwu Agbarakwe"})
